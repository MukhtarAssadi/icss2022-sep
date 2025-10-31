package nl.han.ica.icss.parser;

import nl.han.ica.datastructures.HANStack;
import nl.han.ica.datastructures.IHANStack;
import nl.han.ica.icss.ast.*;
import nl.han.ica.icss.ast.literals.*;
import nl.han.ica.icss.ast.operations.AddOperation;
import nl.han.ica.icss.ast.operations.MultiplyOperation;
import nl.han.ica.icss.ast.operations.SubtractOperation;
import nl.han.ica.icss.ast.selectors.*;

public class ASTListener extends ICSSBaseListener {

	private final AST ast = new AST();
	private final IHANStack<ASTNode> currentContainer = new HANStack<>();
	private final IHANStack<Expression> expressionStack = new HANStack<>(); //apparte stack voor expressions zodat ik ze apart kan afhandelen.

	public ASTListener() {
		currentContainer.push(ast.root);
	}

	public AST getAST() {
		return ast;
	}

	@Override
	public void enterStylesheet(ICSSParser.StylesheetContext ctx) {

	}

	@Override
	public void exitStylesheet(ICSSParser.StylesheetContext ctx) {
		currentContainer.pop();
	}

	@Override
	public void enterVariable_assignment(ICSSParser.Variable_assignmentContext ctx) {
		VariableAssignment assignment = new VariableAssignment();
		assignment.name = new VariableReference(ctx.CAPITAL_IDENT().getText());

		currentContainer.peek().addChild(assignment);
		currentContainer.push(assignment);
	}

	@Override
	public void exitVariable_assignment(ICSSParser.Variable_assignmentContext ctx) {
		if (expressionStack.peek() != null) {
			Expression expr = expressionStack.pop();
			((VariableAssignment) currentContainer.peek()).expression = expr;
		}
		currentContainer.pop();
	}

	@Override
	public void enterStylerule(ICSSParser.StyleruleContext ctx) {
		Stylerule rule = new Stylerule();

		if (ctx.LOWER_IDENT() != null)
			rule.selectors.add(new TagSelector(ctx.LOWER_IDENT().getText()));
		else if (ctx.ID_IDENT() != null)
			rule.selectors.add(new IdSelector(ctx.ID_IDENT().getText()));
		else if (ctx.CLASS_IDENT() != null)
			rule.selectors.add(new ClassSelector(ctx.CLASS_IDENT().getText()));

		currentContainer.peek().addChild(rule);
		currentContainer.push(rule);
	}

	@Override
	public void exitStylerule(ICSSParser.StyleruleContext ctx) {
		currentContainer.pop();
	}

	private void addDeclaration(String propertyName) {
		Declaration decl = new Declaration(propertyName);
		currentContainer.peek().addChild(decl);
		currentContainer.push(decl);
	}

	private void closeDeclaration() {
		currentContainer.pop();
	}

	@Override public void enterColor(ICSSParser.ColorContext ctx) { addDeclaration("color"); }
	@Override public void exitColor(ICSSParser.ColorContext ctx) { closeDeclaration(); }

	@Override public void enterBackground_color(ICSSParser.Background_colorContext ctx) { addDeclaration("background-color"); }
	@Override public void exitBackground_color(ICSSParser.Background_colorContext ctx) { closeDeclaration(); }

	@Override public void enterWidth(ICSSParser.WidthContext ctx) { addDeclaration("width"); }
	@Override public void exitWidth(ICSSParser.WidthContext ctx) { closeDeclaration(); }

	@Override public void enterHeight(ICSSParser.HeightContext ctx) { addDeclaration("height"); }
	@Override public void exitHeight(ICSSParser.HeightContext ctx) { closeDeclaration(); }

	@Override
	public void enterElement(ICSSParser.ElementContext ctx) {
		Expression expr = null;

		if (ctx.PIXELSIZE() != null) expr = new PixelLiteral(ctx.PIXELSIZE().getText());
		else if (ctx.PERCENTAGE() != null) expr = new PercentageLiteral(ctx.PERCENTAGE().getText());
		else if (ctx.COLOR() != null) expr = new ColorLiteral(ctx.COLOR().getText());
		else if (ctx.TRUE() != null) expr = new BoolLiteral(true);
		else if (ctx.FALSE() != null) expr = new BoolLiteral(false);
		else if (ctx.SCALAR() != null) expr = new ScalarLiteral(ctx.SCALAR().getText());
		else if (ctx.CAPITAL_IDENT() != null) expr = new VariableReference(ctx.CAPITAL_IDENT().getText());

		if (expr != null)
			expressionStack.push(expr);
	}


	//bouwt expressie omgekeerd op
	//combineert vermenigvuldigingen en optellen
	@Override
	public void exitExpression(ICSSParser.ExpressionContext ctx) {
		if (ctx.vermenigvuldiging().size() > 1) {
			for (int i = 1; i < ctx.vermenigvuldiging().size(); i++) {
				Expression rhs = expressionStack.pop();
				Expression lhs = expressionStack.pop();

				Expression op;
				if (ctx.PLUS(i - 1) != null)
					op = new AddOperation(lhs, rhs);
				else
					op = new SubtractOperation(lhs, rhs);

				expressionStack.push(op);
			}
		}
		if (expressionStack.peek() != null) {
			Expression finalExpr = expressionStack.pop();
			ASTNode parent = currentContainer.peek();

			if (parent instanceof Declaration) {
				((Declaration) parent).expression = finalExpr;
			} else if (parent instanceof VariableAssignment) {
				((VariableAssignment) parent).expression = finalExpr;
			} else if (parent instanceof IfClause) {
				((IfClause) parent).conditionalExpression = finalExpr;
			}

		}
	}

	@Override
	public void exitVermenigvuldiging(ICSSParser.VermenigvuldigingContext ctx) {
		if (ctx.element().size() > 1) {
			Expression rhs = expressionStack.pop();
			Expression lhs = expressionStack.pop();
			Expression result = new MultiplyOperation(lhs, rhs);
			expressionStack.push(result);
		}
	}

	@Override
	public void enterIf_statement (ICSSParser.If_statementContext ctx){
		IfClause ifClause = new IfClause();
		if (ctx.TRUE() != null)
			ifClause.conditionalExpression = new BoolLiteral(true);
		else if (ctx.FALSE() != null)
			ifClause.conditionalExpression = new BoolLiteral(false);
		else if (ctx.CAPITAL_IDENT() != null)
			ifClause.conditionalExpression = new VariableReference(ctx.CAPITAL_IDENT().getText());

		currentContainer.peek().addChild(ifClause);
		currentContainer.push(ifClause);
	}

	@Override
	public void exitIf_statement (ICSSParser.If_statementContext ctx){
		currentContainer.pop();
	}

	@Override
	public void enterElse_statement (ICSSParser.Else_statementContext ctx){
		ElseClause elseClause = new ElseClause();
		currentContainer.peek().addChild(elseClause);
		currentContainer.push(elseClause);
	}

	@Override
	public void exitElse_statement (ICSSParser.Else_statementContext ctx){
		currentContainer.pop();
	}
}

