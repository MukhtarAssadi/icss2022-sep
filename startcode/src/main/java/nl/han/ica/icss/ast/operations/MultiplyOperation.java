package nl.han.ica.icss.ast.operations;

import nl.han.ica.icss.ast.Expression;
import nl.han.ica.icss.ast.Operation;

public class MultiplyOperation extends Operation {

    @Override
    public String getNodeLabel() {
        return "Multiply";
    }

    public MultiplyOperation(Expression lhs, Expression rhs) {
        this.lhs = lhs;
        this.rhs = rhs;
    }
}
