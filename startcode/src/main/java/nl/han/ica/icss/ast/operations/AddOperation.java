package nl.han.ica.icss.ast.operations;

import nl.han.ica.icss.ast.Expression;
import nl.han.ica.icss.ast.Operation;

public class AddOperation extends Operation {

    public AddOperation() {

    }

    @Override
    public String getNodeLabel() {
        return "Add";
    }

    public AddOperation(Expression lhs, Expression rhs) {
        this.lhs = lhs;
        this.rhs = rhs;
    }
}
