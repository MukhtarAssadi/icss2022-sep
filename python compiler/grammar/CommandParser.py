# Generated from Command.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,39,8,1,1,2,1,2,1,
        2,3,2,44,8,2,1,2,1,2,1,2,3,2,49,8,2,1,2,1,2,1,2,3,2,54,8,2,1,2,1,
        2,3,2,58,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,68,8,3,1,4,1,4,
        1,4,1,4,3,4,74,8,4,1,5,1,5,1,5,1,5,1,5,3,5,81,8,5,1,6,1,6,1,7,1,
        7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,
        20,0,6,1,0,11,12,1,0,16,19,1,0,20,25,1,0,26,28,1,0,29,31,1,0,32,
        34,102,0,22,1,0,0,0,2,38,1,0,0,0,4,57,1,0,0,0,6,67,1,0,0,0,8,73,
        1,0,0,0,10,80,1,0,0,0,12,82,1,0,0,0,14,84,1,0,0,0,16,86,1,0,0,0,
        18,88,1,0,0,0,20,90,1,0,0,0,22,27,3,2,1,0,23,24,5,35,0,0,24,26,3,
        2,1,0,25,23,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,
        30,1,0,0,0,29,27,1,0,0,0,30,31,5,0,0,1,31,1,1,0,0,0,32,39,3,4,2,
        0,33,39,3,10,5,0,34,39,3,14,7,0,35,39,3,16,8,0,36,39,3,18,9,0,37,
        39,3,20,10,0,38,32,1,0,0,0,38,33,1,0,0,0,38,34,1,0,0,0,38,35,1,0,
        0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,3,1,0,0,0,40,41,5,1,0,0,41,43,
        3,6,3,0,42,44,5,2,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,
        45,48,3,8,4,0,46,47,5,3,0,0,47,49,3,8,4,0,48,46,1,0,0,0,48,49,1,
        0,0,0,49,58,1,0,0,0,50,51,5,4,0,0,51,53,3,6,3,0,52,54,5,2,0,0,53,
        52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,3,8,4,0,56,58,1,0,0,
        0,57,40,1,0,0,0,57,50,1,0,0,0,58,5,1,0,0,0,59,68,5,5,0,0,60,61,5,
        6,0,0,61,68,5,36,0,0,62,63,5,7,0,0,63,68,5,36,0,0,64,68,5,8,0,0,
        65,68,5,9,0,0,66,68,5,10,0,0,67,59,1,0,0,0,67,60,1,0,0,0,67,62,1,
        0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,7,1,0,0,0,69,
        74,3,10,5,0,70,74,3,14,7,0,71,74,3,16,8,0,72,74,3,20,10,0,73,69,
        1,0,0,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,9,1,0,0,0,75,
        76,7,0,0,0,76,81,3,12,6,0,77,81,5,13,0,0,78,81,5,14,0,0,79,81,5,
        15,0,0,80,75,1,0,0,0,80,77,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,
        11,1,0,0,0,82,83,7,1,0,0,83,13,1,0,0,0,84,85,7,2,0,0,85,15,1,0,0,
        0,86,87,7,3,0,0,87,17,1,0,0,0,88,89,7,4,0,0,89,19,1,0,0,0,90,91,
        7,5,0,0,91,21,1,0,0,0,9,27,38,43,48,53,57,67,73,80
    ]

class CommandParser ( Parser ):

    grammarFileName = "Command.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "','", "'else'", "'when'", "'opponent low existence'", 
                     "'opponent existence below'", "'you have existence below'", 
                     "'you have no entities'", "'your hand is full'", "'opponent has many entities'", 
                     "'play'", "'use'", "'save energy'", "'spend all energy'", 
                     "'play cards only if you have enough energy'", "'cheap cards'", 
                     "'cheap entities'", "'technologies'", "'entities first'", 
                     "'attack player'", "'attack opponent directly'", "'attack weakest entity'", 
                     "'attack lowest hp entity'", "'attack highest power entity'", 
                     "'if no entities, attack player'", "'play careful until opponent low existence'", 
                     "'finish opponent when low existence'", "'go all in when opponent low existence'", 
                     "'play on hard mode'", "'play on normal mode'", "'play on easy mode'", 
                     "'be aggressive'", "'play defensive'", "'be cautious'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "CONJ", "INT", 
                      "WS" ]

    RULE_command = 0
    RULE_statement = 1
    RULE_conditional = 2
    RULE_condition = 3
    RULE_action = 4
    RULE_playInstr = 5
    RULE_play_target = 6
    RULE_attackInstr = 7
    RULE_existenceInstr = 8
    RULE_difficultyInstr = 9
    RULE_styleInstr = 10

    ruleNames =  [ "command", "statement", "conditional", "condition", "action", 
                   "playInstr", "play_target", "attackInstr", "existenceInstr", 
                   "difficultyInstr", "styleInstr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    CONJ=35
    INT=36
    WS=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.StatementContext)
            else:
                return self.getTypedRuleContext(CommandParser.StatementContext,i)


        def EOF(self):
            return self.getToken(CommandParser.EOF, 0)

        def CONJ(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.CONJ)
            else:
                return self.getToken(CommandParser.CONJ, i)

        def getRuleIndex(self):
            return CommandParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = CommandParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.statement()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 23
                self.match(CommandParser.CONJ)
                self.state = 24
                self.statement()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(CommandParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional(self):
            return self.getTypedRuleContext(CommandParser.ConditionalContext,0)


        def playInstr(self):
            return self.getTypedRuleContext(CommandParser.PlayInstrContext,0)


        def attackInstr(self):
            return self.getTypedRuleContext(CommandParser.AttackInstrContext,0)


        def existenceInstr(self):
            return self.getTypedRuleContext(CommandParser.ExistenceInstrContext,0)


        def difficultyInstr(self):
            return self.getTypedRuleContext(CommandParser.DifficultyInstrContext,0)


        def styleInstr(self):
            return self.getTypedRuleContext(CommandParser.StyleInstrContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CommandParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.conditional()
                pass
            elif token in [11, 12, 13, 14, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.playInstr()
                pass
            elif token in [20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.attackInstr()
                pass
            elif token in [26, 27, 28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.existenceInstr()
                pass
            elif token in [29, 30, 31]:
                self.enterOuterAlt(localctx, 5)
                self.state = 36
                self.difficultyInstr()
                pass
            elif token in [32, 33, 34]:
                self.enterOuterAlt(localctx, 6)
                self.state = 37
                self.styleInstr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(CommandParser.ConditionContext,0)


        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.ActionContext)
            else:
                return self.getTypedRuleContext(CommandParser.ActionContext,i)


        def getRuleIndex(self):
            return CommandParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = CommandParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(CommandParser.T__0)
                self.state = 41
                self.condition()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 42
                    self.match(CommandParser.T__1)


                self.state = 45
                self.action()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 46
                    self.match(CommandParser.T__2)
                    self.state = 47
                    self.action()


                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(CommandParser.T__3)
                self.state = 51
                self.condition()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 52
                    self.match(CommandParser.T__1)


                self.state = 55
                self.action()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CommandParser.INT, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = CommandParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(CommandParser.T__4)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(CommandParser.T__5)
                self.state = 61
                self.match(CommandParser.INT)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.match(CommandParser.T__6)
                self.state = 63
                self.match(CommandParser.INT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.match(CommandParser.T__7)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                self.match(CommandParser.T__8)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.match(CommandParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def playInstr(self):
            return self.getTypedRuleContext(CommandParser.PlayInstrContext,0)


        def attackInstr(self):
            return self.getTypedRuleContext(CommandParser.AttackInstrContext,0)


        def existenceInstr(self):
            return self.getTypedRuleContext(CommandParser.ExistenceInstrContext,0)


        def styleInstr(self):
            return self.getTypedRuleContext(CommandParser.StyleInstrContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = CommandParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_action)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.playInstr()
                pass
            elif token in [20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.attackInstr()
                pass
            elif token in [26, 27, 28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.existenceInstr()
                pass
            elif token in [32, 33, 34]:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.styleInstr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlayInstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def play_target(self):
            return self.getTypedRuleContext(CommandParser.Play_targetContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_playInstr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayInstr" ):
                listener.enterPlayInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayInstr" ):
                listener.exitPlayInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlayInstr" ):
                return visitor.visitPlayInstr(self)
            else:
                return visitor.visitChildren(self)




    def playInstr(self):

        localctx = CommandParser.PlayInstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_playInstr)
        self._la = 0 # Token type
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 76
                self.play_target()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(CommandParser.T__12)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.match(CommandParser.T__13)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.match(CommandParser.T__14)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Play_targetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_play_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlay_target" ):
                listener.enterPlay_target(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlay_target" ):
                listener.exitPlay_target(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlay_target" ):
                return visitor.visitPlay_target(self)
            else:
                return visitor.visitChildren(self)




    def play_target(self):

        localctx = CommandParser.Play_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_play_target)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttackInstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_attackInstr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttackInstr" ):
                listener.enterAttackInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttackInstr" ):
                listener.exitAttackInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttackInstr" ):
                return visitor.visitAttackInstr(self)
            else:
                return visitor.visitChildren(self)




    def attackInstr(self):

        localctx = CommandParser.AttackInstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attackInstr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExistenceInstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_existenceInstr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExistenceInstr" ):
                listener.enterExistenceInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExistenceInstr" ):
                listener.exitExistenceInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExistenceInstr" ):
                return visitor.visitExistenceInstr(self)
            else:
                return visitor.visitChildren(self)




    def existenceInstr(self):

        localctx = CommandParser.ExistenceInstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_existenceInstr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DifficultyInstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_difficultyInstr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDifficultyInstr" ):
                listener.enterDifficultyInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDifficultyInstr" ):
                listener.exitDifficultyInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDifficultyInstr" ):
                return visitor.visitDifficultyInstr(self)
            else:
                return visitor.visitChildren(self)




    def difficultyInstr(self):

        localctx = CommandParser.DifficultyInstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_difficultyInstr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StyleInstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_styleInstr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStyleInstr" ):
                listener.enterStyleInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStyleInstr" ):
                listener.exitStyleInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStyleInstr" ):
                return visitor.visitStyleInstr(self)
            else:
                return visitor.visitChildren(self)




    def styleInstr(self):

        localctx = CommandParser.StyleInstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_styleInstr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





