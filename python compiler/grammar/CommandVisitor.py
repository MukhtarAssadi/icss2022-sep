# Generated from Command.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CommandParser import CommandParser
else:
    from CommandParser import CommandParser

# This class defines a complete generic visitor for a parse tree produced by CommandParser.

class CommandVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CommandParser#command.
    def visitCommand(self, ctx:CommandParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#statement.
    def visitStatement(self, ctx:CommandParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#conditional.
    def visitConditional(self, ctx:CommandParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#condition.
    def visitCondition(self, ctx:CommandParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#action.
    def visitAction(self, ctx:CommandParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#playInstr.
    def visitPlayInstr(self, ctx:CommandParser.PlayInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#play_target.
    def visitPlay_target(self, ctx:CommandParser.Play_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#attackInstr.
    def visitAttackInstr(self, ctx:CommandParser.AttackInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#existenceInstr.
    def visitExistenceInstr(self, ctx:CommandParser.ExistenceInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#difficultyInstr.
    def visitDifficultyInstr(self, ctx:CommandParser.DifficultyInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#styleInstr.
    def visitStyleInstr(self, ctx:CommandParser.StyleInstrContext):
        return self.visitChildren(ctx)



del CommandParser