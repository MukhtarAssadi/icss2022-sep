# Generated from Command.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CommandParser import CommandParser
else:
    from CommandParser import CommandParser

# This class defines a complete listener for a parse tree produced by CommandParser.
class CommandListener(ParseTreeListener):

    # Enter a parse tree produced by CommandParser#command.
    def enterCommand(self, ctx:CommandParser.CommandContext):
        pass

    # Exit a parse tree produced by CommandParser#command.
    def exitCommand(self, ctx:CommandParser.CommandContext):
        pass


    # Enter a parse tree produced by CommandParser#statement.
    def enterStatement(self, ctx:CommandParser.StatementContext):
        pass

    # Exit a parse tree produced by CommandParser#statement.
    def exitStatement(self, ctx:CommandParser.StatementContext):
        pass


    # Enter a parse tree produced by CommandParser#conditional.
    def enterConditional(self, ctx:CommandParser.ConditionalContext):
        pass

    # Exit a parse tree produced by CommandParser#conditional.
    def exitConditional(self, ctx:CommandParser.ConditionalContext):
        pass


    # Enter a parse tree produced by CommandParser#condition.
    def enterCondition(self, ctx:CommandParser.ConditionContext):
        pass

    # Exit a parse tree produced by CommandParser#condition.
    def exitCondition(self, ctx:CommandParser.ConditionContext):
        pass


    # Enter a parse tree produced by CommandParser#action.
    def enterAction(self, ctx:CommandParser.ActionContext):
        pass

    # Exit a parse tree produced by CommandParser#action.
    def exitAction(self, ctx:CommandParser.ActionContext):
        pass


    # Enter a parse tree produced by CommandParser#playInstr.
    def enterPlayInstr(self, ctx:CommandParser.PlayInstrContext):
        pass

    # Exit a parse tree produced by CommandParser#playInstr.
    def exitPlayInstr(self, ctx:CommandParser.PlayInstrContext):
        pass


    # Enter a parse tree produced by CommandParser#play_target.
    def enterPlay_target(self, ctx:CommandParser.Play_targetContext):
        pass

    # Exit a parse tree produced by CommandParser#play_target.
    def exitPlay_target(self, ctx:CommandParser.Play_targetContext):
        pass


    # Enter a parse tree produced by CommandParser#attackInstr.
    def enterAttackInstr(self, ctx:CommandParser.AttackInstrContext):
        pass

    # Exit a parse tree produced by CommandParser#attackInstr.
    def exitAttackInstr(self, ctx:CommandParser.AttackInstrContext):
        pass


    # Enter a parse tree produced by CommandParser#existenceInstr.
    def enterExistenceInstr(self, ctx:CommandParser.ExistenceInstrContext):
        pass

    # Exit a parse tree produced by CommandParser#existenceInstr.
    def exitExistenceInstr(self, ctx:CommandParser.ExistenceInstrContext):
        pass


    # Enter a parse tree produced by CommandParser#difficultyInstr.
    def enterDifficultyInstr(self, ctx:CommandParser.DifficultyInstrContext):
        pass

    # Exit a parse tree produced by CommandParser#difficultyInstr.
    def exitDifficultyInstr(self, ctx:CommandParser.DifficultyInstrContext):
        pass


    # Enter a parse tree produced by CommandParser#styleInstr.
    def enterStyleInstr(self, ctx:CommandParser.StyleInstrContext):
        pass

    # Exit a parse tree produced by CommandParser#styleInstr.
    def exitStyleInstr(self, ctx:CommandParser.StyleInstrContext):
        pass



del CommandParser