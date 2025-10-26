package nl.han.ica.icss.checker;

import nl.han.ica.datastructures.IHANLinkedList;
import nl.han.ica.icss.ast.AST;
import nl.han.ica.icss.ast.types.ExpressionType;

import java.util.HashMap;



public class Checker {

    private IHANLinkedList<HashMap<String, ExpressionType>> variableTypes;

    public void check(AST ast) {
        checkStylesheet(ast.root);
    }

    public void checkStylesheet(Stylesheet node){
        
        checkStatement((Statement) node.getChildren());
    }

    public void checkStatement(Statement node){
        checkVariableAssignment(?);
        checkStylerule(?);
    }

    public void checkVariableAssignment(VariableAssignment node){
        checkExpressie(?);
    }

    public void checkExpressie(Expressie node){

    }

    public void checkStylerule(Stylerule node){
        checkProperty(?);
        checkIfStatement(?);
    }

    public void checkProperty(Property node){
        // color | background_color | width | height
    }

    public void checkIfStatement(IfStatement node) {
        checkProperty(?);
        checkIfStatement(?);
        checkElseStatement(?);
    }

    public void checkElseStatement(ElseStatement node){
        checkProperty(?);
        checkIfStatement(?);
    }

}
