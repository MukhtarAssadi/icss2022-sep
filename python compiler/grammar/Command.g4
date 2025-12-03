grammar Command;

command
    : statement (CONJ statement)* EOF
    ;

statement
    : conditional
    | playInstr
    | attackInstr
    | existenceInstr
    | difficultyInstr
    | styleInstr
    ;


conditional
    : 'if' condition ','? action ('else' action)?
    | 'when' condition ','? action
    ;

condition
    : 'opponent low existence'
    | 'opponent existence below' INT
    | 'you have existence below' INT
    | 'you have no entities'
    | 'your hand is full'
    | 'opponent has many entities'
    ;

action
    : playInstr
    | attackInstr
    | existenceInstr
    | styleInstr
    ;


playInstr
    : ('play' | 'use') play_target
    | 'save energy'
    | 'spend all energy'
    | 'play cards'
    ;

play_target
    : 'cheap cards'
    | 'cheap entities'
    | 'technologies'
    | 'entities first'
    ;


attackInstr
    : 'attack player'
    | 'attack opponent directly'
    | 'attack weakest entity'
    | 'attack lowest hp entity'
    | 'attack highest power entity'
    | 'if no entities, attack player'
    ;


existenceInstr
    : 'play careful until opponent low existence'
    | 'finish opponent when low existence'
    | 'go all in when opponent low existence'
    ;


difficultyInstr
    : 'play on hard mode'
    | 'play on normal mode'
    | 'play on easy mode'
    ;

styleInstr
    : 'be aggressive'
    | 'play defensive'
    | 'be cautious'
    ;


CONJ : 'and' | 'then' | 'also' ;
INT  : [0-9]+ ;

WS   : [ \t\r\n]+ -> skip ;