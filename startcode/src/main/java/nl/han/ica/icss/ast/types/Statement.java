package nl.han.ica.icss.ast;

import java.util.ArrayList;

public abstract class Statement extends ASTNode {

    @Override
    public String getNodeLabel() {
        return "Statement";
    }

    @Override
    public ArrayList<ASTNode> getChildren() {
        return new ArrayList<>();
    }

    @Override
    public ASTNode addChild(ASTNode child) {
        return this;
    }
}