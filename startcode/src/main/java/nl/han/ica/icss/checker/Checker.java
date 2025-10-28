package nl.han.ica.icss.checker;

import nl.han.ica.datastructures.IHANLinkedList;
import nl.han.ica.icss.ast.AST;
import nl.han.ica.icss.ast.AST.*;
import nl.han.ica.icss.ast.types.ExpressionType;

import nl.han.ica.icss.ast.ASTNode;
import nl.han.ica.icss.ast.Stylesheet;
import nl.han.ica.icss.ast.Statement;
import nl.han.ica.icss.ast.Stylerule;
import nl.han.ica.icss.ast.VariableAssignment;
import nl.han.ica.icss.ast.VariableReference;
import nl.han.ica.icss.ast.Declaration;
import nl.han.ica.icss.ast.Expression;
import nl.han.ica.icss.ast.Operation;
import nl.han.ica.icss.ast.operations.AddOperation;
import nl.han.ica.icss.ast.operations.SubtractOperation;
import nl.han.ica.icss.ast.operations.MultiplyOperation;
import nl.han.ica.icss.ast.literals.BoolLiteral;
import nl.han.ica.icss.ast.literals.ColorLiteral;
import nl.han.ica.icss.ast.literals.PixelLiteral;
import nl.han.ica.icss.ast.literals.PercentageLiteral;
import nl.han.ica.icss.ast.literals.ScalarLiteral;
import nl.han.ica.icss.ast.IfClause;
import nl.han.ica.icss.ast.ElseClause;

import java.util.HashMap;


// to do
// Voeg IHANLinkedList toe aan checkVariableAssignment
// bepaal het type expressie in checkExpression (recursief)
// zorg dat checkProperty kijkt of het de juiste property heeft (color moet een kleur zijn, geen width)
// zorg dat checkIfStatement en Else alleen een boolean kan hebben als conditional
// zorg dat checkStylerule de linked lists maakt voor de scopes van variabelen
// variableTypes stack global	zorgt ervoor dat de scope per block in scope blijft







public class Checker {

//    private IHANLinkedList<HashMap<String, ExpressionType>> variableTypes;

    public void check(AST ast) {
        checkStylesheet(ast.root);
    }

    public void checkStylesheet(Stylesheet node){
        for (ASTNode child : node.getChildren()) {
            if (child instanceof Statement) {
                checkStatement((Statement) child);
            }
        }
    }

    public void checkStatement(Statement node){
        if (node instanceof VariableAssignment) {
            checkVariableAssignment((VariableAssignment) node);
        } else if (node instanceof Stylerule) {
            checkStylerule((Stylerule) node);
        }
    }

    //a := 10px
    public void checkVariableAssignment(VariableAssignment node){
        checkExpression(node.expression);
        //gebruik hier HANLinkedlist om de variabele op te slaan
    }

    public void checkExpression(Expression node){
        if (node instanceof Operation) {
            Operation op = (Operation) node;
            checkExpression(op.lhs);
            checkExpression(op.rhs);
            //kijk of de 2 variabele valide zijn in deze expressie
        } else if (node instanceof VariableReference) {
            //kijk of de variabele in variableTypes staat
        }
    }

    private void checkStylerule(Stylerule node) {
//        variableTypes.addFirst(new HashMap<>());
        for (ASTNode child : node.getChildren()) {
            if (child instanceof Declaration) {
                checkProperty((Declaration) child);
            } else if (child instanceof IfClause) {
                checkIfStatement((IfClause) child);
            }
        }
//        variableTypes.removeFirst();
    }

    public void checkProperty(Declaration node){
        checkExpression(node.expression);
        //kijk of de juiste type gebruikt wordt
    }

    public void checkIfStatement(IfClause node) {
        checkExpression(node.conditionalExpression);
//        variableTypes.addFirst(new HashMap<>());
        for (ASTNode child : node.getChildren()) {
            if (child instanceof Declaration) {
            checkProperty((Declaration) child);
            } else if (child instanceof IfClause) {
            checkIfStatement((IfClause) child);
            } else if (child instanceof ElseClause) {
            checkElseStatement((ElseClause) child);
         }
    }
//        variableTypes.removeFirst();
}
    private void checkElseStatement(ElseClause node) {
//        variableTypes.addFirst(new HashMap<>());
        for (ASTNode child : node.getChildren()) {
            if (child instanceof Declaration) {
                checkProperty((Declaration) child);
            } else if (child instanceof IfClause) {
                checkIfStatement((IfClause) child);
            }
        }
//        variableTypes.removeFirst();
    }

}
