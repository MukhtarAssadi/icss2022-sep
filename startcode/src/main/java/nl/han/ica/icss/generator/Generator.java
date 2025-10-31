package nl.han.ica.icss.generator;


import nl.han.ica.icss.ast.*;
import nl.han.ica.icss.ast.literals.*;

public class Generator {

	public String generate(AST ast) {
		StringBuilder builder = new StringBuilder();
		Stylesheet root = ast.root;

		for (ASTNode node : root.body) {
			if (node instanceof Stylerule) {
				builder.append(generateStylerule((Stylerule) node));
			}
		}

		return builder.toString().trim();
	}

	private String generateStylerule(Stylerule rule) {
		StringBuilder builder = new StringBuilder();

		for (Selector selector : rule.selectors) {
			builder.append(selector.toString()).append(" {\n");
		}

		for (ASTNode child : rule.body) {
			if (child instanceof Declaration) {
				builder.append("  ")
						.append(generateDeclaration((Declaration) child))
						.append("\n");
			}
		}

		builder.append("}\n\n");
		return builder.toString();
	}

	private String generateDeclaration(Declaration decl) {
		return decl.property.name + ": " + literalToString(decl.expression) + ";";
	}

	private String literalToString(Expression expr) {
		if (expr instanceof ColorLiteral)      return ((ColorLiteral) expr).value;
		if (expr instanceof PixelLiteral)      return ((PixelLiteral) expr).value + "px";
		if (expr instanceof PercentageLiteral) return ((PercentageLiteral) expr).value + "%";
		if (expr instanceof BoolLiteral)       return ((BoolLiteral) expr).value ? "TRUE" : "FALSE";
		if (expr instanceof ScalarLiteral)     return String.valueOf(((ScalarLiteral) expr).value);
		return "";
	}

	
}
