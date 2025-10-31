package nl.han.ica.icss.transforms;

import nl.han.ica.datastructures.HANLinkedList;
import nl.han.ica.datastructures.IHANLinkedList;
import nl.han.ica.icss.ast.*;
import nl.han.ica.icss.ast.literals.BoolLiteral;
import nl.han.ica.icss.ast.literals.PercentageLiteral;
import nl.han.ica.icss.ast.literals.PixelLiteral;
import nl.han.ica.icss.ast.literals.ScalarLiteral;
import nl.han.ica.icss.ast.operations.AddOperation;
import nl.han.ica.icss.ast.operations.MultiplyOperation;
import nl.han.ica.icss.ast.operations.SubtractOperation;

import java.util.HashMap;

public class Evaluator implements Transform {

    private IHANLinkedList<HashMap<String, Literal>> variableValues = new HANLinkedList<>();

    @Override
    public void apply(AST ast) {
        variableValues.addFirst(new HashMap<>());
        evaluateStylesheet(ast.root);
        ast.root.body.removeIf(node -> node instanceof VariableAssignment);
        variableValues.removeFirst();
    }

    private void evaluateStylesheet(Stylesheet stylesheet) {
        for (ASTNode child : stylesheet.body) {
            if (child instanceof VariableAssignment)
                evaluateVariableAssignment((VariableAssignment) child);
            else if (child instanceof Stylerule)
                evaluateStylerule((Stylerule) child);
        }
    }

    private void evaluateStylerule(Stylerule rule) {
        variableValues.addFirst(new HashMap<>());

        var children = new java.util.ArrayList<>(rule.body); //kopie anders kan variableValues breken

        for (ASTNode child : children) {
            if (child instanceof Declaration)
                evaluateDeclaration((Declaration) child);
            else if (child instanceof IfClause)
                evaluateIfClause(rule, (IfClause) child);
            else if (child instanceof VariableAssignment)
                evaluateVariableAssignment((VariableAssignment) child);
        }

        variableValues.removeFirst();
    }

    private void evaluateVariableAssignment(VariableAssignment node) {
        Literal value = evaluateExpression(node.expression);
        if (value != null)
            variableValues.getFirst().put(node.name.name, value);
    }

    private void evaluateIfClause(Stylerule parent, IfClause node) {
        Literal condition = evaluateExpression(node.conditionalExpression);
        boolean conditionValue = (condition instanceof BoolLiteral) && ((BoolLiteral) condition).value; //check True of False

        var body = conditionValue ? node.body : node.elseClause != null ? node.elseClause.body : null; //check if, else of niks
        if (body == null) return;

        for (ASTNode child : body) {
            if (child instanceof Declaration)
                parent.body.add(copyDeclaration((Declaration) child));
            else if (child instanceof IfClause)
                evaluateIfClause(parent, (IfClause) child);
        }
    }

    private void evaluateDeclaration(Declaration node) {
        node.expression = evaluateExpression(node.expression);
    }

    private Declaration copyDeclaration(Declaration original) {
        Declaration copy = new Declaration(original.property.name);
        copy.expression = evaluateExpression(original.expression);
        return copy;
    }

    private Literal evaluateExpression(Expression expr) {
        if (expr instanceof Literal)
            return (Literal) expr;

        if (expr instanceof VariableReference)
            return resolveVariable((VariableReference) expr);

        if (expr instanceof Operation)
            return evaluateOperation((Operation) expr);

        return null;
    }

    private Literal resolveVariable(VariableReference ref) {
        for (int i = 0; i < variableValues.getSize(); i++) {
            var scope = variableValues.get(i);
            if (scope.containsKey(ref.name))
                return scope.get(ref.name);
        }
        return null;
    }

    private Literal evaluateOperation(Operation op) {
        Literal left = evaluateExpression(op.lhs);
        Literal right = evaluateExpression(op.rhs);
        if (left == null || right == null) return null;

        int result = calculateValue(op, left, right);
        String type = determineLiteralType(left, right);

        switch (type) {
            case "px":
                return new PixelLiteral(result);
            case "%":
                return new PercentageLiteral(result);
            default:
                return new ScalarLiteral(result);
        }
    }

    private String determineLiteralType(Literal left, Literal right) {
        if (left instanceof PixelLiteral || right instanceof PixelLiteral) return "px";
        if (left instanceof PercentageLiteral || right instanceof PercentageLiteral) return "%";
        return "scalar";
    }

    private int calculateValue(Operation op, Literal left, Literal right) {
        int lv = getValue(left);
        int rv = getValue(right);

        if (op instanceof AddOperation) return lv + rv;
        if (op instanceof SubtractOperation) return lv - rv;
        if (op instanceof MultiplyOperation) return lv * rv;

        return 0;
    }

    private int getValue(Literal lit) {
        if (lit instanceof PixelLiteral) return ((PixelLiteral) lit).value;
        if (lit instanceof PercentageLiteral) return ((PercentageLiteral) lit).value;
        if (lit instanceof ScalarLiteral) return ((ScalarLiteral) lit).value;
        return 0;
    }
}
