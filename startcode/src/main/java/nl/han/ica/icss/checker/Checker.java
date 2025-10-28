package nl.han.ica.icss.checker;

import nl.han.ica.datastructures.HANLinkedList;
import nl.han.ica.datastructures.IHANLinkedList;
import nl.han.ica.icss.ast.AST;

import nl.han.ica.icss.ast.ASTNode;
import nl.han.ica.icss.ast.Stylesheet;
import nl.han.ica.icss.ast.Stylerule;
import nl.han.ica.icss.ast.VariableAssignment;
import nl.han.ica.icss.ast.VariableReference;
import nl.han.ica.icss.ast.Declaration;
import nl.han.ica.icss.ast.Expression;
import nl.han.ica.icss.ast.Operation;
import nl.han.ica.icss.ast.IfClause;
import nl.han.ica.icss.ast.ElseClause;
import nl.han.ica.icss.ast.literals.*;
import nl.han.ica.icss.ast.types.ExpressionType;

import java.util.HashMap;


// to do
// Voeg IHANLinkedList toe aan checkVariableAssignment
// bepaal het type expressie in checkExpression (recursief)
// zorg dat checkProperty kijkt of het de juiste property heeft (color moet een kleur zijn, geen width)
// zorg dat checkIfStatement en Else alleen een boolean kan hebben als conditional
// zorg dat checkStylerule de linked lists maakt voor de scopes van variabelen
// variableTypes stack global	zorgt ervoor dat de scope per block in scope blijft







public class Checker {

    private IHANLinkedList<HashMap<String, ExpressionType>> variableTypes = new HANLinkedList<>();

    public void check(AST ast) {
        variableTypes.addFirst(new HashMap<>());
        checkStylesheet(ast.root);
        variableTypes.removeFirst();
    }

    public void checkStylesheet(Stylesheet node){
        for (ASTNode child : node.body) {
            if (child instanceof VariableAssignment) {
                checkVariableAssignment((VariableAssignment) child);
            } else if (child instanceof Stylerule) {
                checkStylerule((Stylerule) child);
            }
        }
    }

    //a := 10px
    public void checkVariableAssignment(VariableAssignment node){
        ExpressionType type = checkExpression(node.expression);
        if (type != null && type != ExpressionType.UNDEFINED){
            variableTypes.getFirst().put(node.name.name, type);
        }
        else {
            node.setError("Undefined expression in variable assignment");
        }
    }

    public ExpressionType checkExpression(Expression node){
        if (node == null)
        {return ExpressionType.UNDEFINED;}

        if (node instanceof PixelLiteral) {return ExpressionType.PIXEL;}
        if (node instanceof PercentageLiteral) {return ExpressionType.PERCENTAGE;}
        if (node instanceof ColorLiteral) {return ExpressionType.COLOR;}
        if (node instanceof BoolLiteral) {return ExpressionType.BOOL;}
        if (node instanceof ScalarLiteral) {return ExpressionType.SCALAR;}

        if (node instanceof VariableReference) {
            return checkVariableReference((VariableReference) node);
        }

        if (node instanceof Operation) {
            return checkOperation((Operation) node);
        }

        node.setError("Unknown expression type");
        return null;
    }

    private void checkStylerule(Stylerule node) {
        variableTypes.addFirst(new HashMap<>());
        for (ASTNode child : node.getChildren()) {
            if (child instanceof Declaration) {
                checkPropertyDeclaration((Declaration) child);
            } else if (child instanceof IfClause) {
                checkIfStatement((IfClause) child);
            } else if (child instanceof VariableAssignment) {
                checkVariableAssignment((VariableAssignment) child);
            }
        }
        variableTypes.removeFirst();
    }

    public void checkPropertyDeclaration(Declaration node){
        ExpressionType valueType = checkExpression(node.expression);
        if (valueType == ExpressionType.UNDEFINED){
            return;
        }
        String propertyname = node.property.name;
        switch (propertyname) {
            case "color":
            case "background-color":
                if (valueType != ExpressionType.COLOR) {
                    node.setError("Property '" + propertyname+ "' must be a color.");
                }
                break;

            case "width":
            case "height":
                if (valueType != ExpressionType.PIXEL && valueType != ExpressionType.PERCENTAGE) {
                    node.setError("Property '" + propertyname + "' must be pixel or percentage value.");
                }
                break;
            default:
                node.setError("Unknown property: '" + propertyname + "'");
        }
    }

    public void checkIfStatement(IfClause node) {
        ExpressionType conditionType = checkExpression(node.conditionalExpression);
        if (conditionType != ExpressionType.BOOL) {
            node.setError("If condition must be a boolean expression.");
        }

        variableTypes.addFirst(new HashMap<>());
        for (ASTNode child : node.body) {
            if (child instanceof Declaration) {
            checkPropertyDeclaration((Declaration) child);
            } else if (child instanceof VariableAssignment) {
            checkVariableAssignment((VariableAssignment) child);
            } else if (child instanceof IfClause) {
            checkIfStatement((IfClause) child);
         }
            variableTypes.removeFirst();

            if (node.elseClause != null) {
                checkElseStatement(node.elseClause);
            }
    }

}
    private void checkElseStatement(ElseClause node) {
        variableTypes.addFirst(new HashMap<>());
        for (ASTNode child : node.getChildren()) {
            if (child instanceof Declaration) {
                checkPropertyDeclaration((Declaration) child);
            } else if (child instanceof IfClause) {
                checkIfStatement((IfClause) child);
            }
        }
        variableTypes.removeFirst();
    }

}
