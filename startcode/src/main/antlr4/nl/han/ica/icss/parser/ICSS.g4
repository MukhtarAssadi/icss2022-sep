grammar ICSS;

//--- LEXER: ---

// IF support:
IF: 'if';
ELSE: 'else';
BOX_BRACKET_OPEN: '[';
BOX_BRACKET_CLOSE: ']';


//Literals
TRUE: 'TRUE';
FALSE: 'FALSE';
PIXELSIZE: [0-9]+ 'px';
PERCENTAGE: [0-9]+ '%';
SCALAR: [0-9]+;


//Color value takes precedence over id idents
COLOR: '#' [0-9a-f] [0-9a-f] [0-9a-f] [0-9a-f] [0-9a-f] [0-9a-f];

//Specific identifiers for id's and css classes
ID_IDENT: '#' [a-z0-9\-]+;
CLASS_IDENT: '.' [a-z0-9\-]+;

//General identifiers
LOWER_IDENT: [a-z] [a-z0-9\-]*;
CAPITAL_IDENT: [A-Z] [A-Za-z0-9_]*;

//All whitespace is skipped
WS: [ \t\r\n]+ -> skip;

//
OPEN_BRACE: '{';
CLOSE_BRACE: '}';
SEMICOLON: ';';
COLON: ':';
PLUS: '+';
MIN: '-';
MUL: '*';
ASSIGNMENT_OPERATOR: ':=';

variable_value: COLOR | PIXELSIZE | PERCENTAGE | SCALAR | TRUE | FALSE;

//--- PARSER: ---
stylesheet: (statement)*;
statement: stylerule | variable_assignment;

color: 'color:' (COLOR | CAPITAL_IDENT);
background_color: 'background-color:' (COLOR | CAPITAL_IDENT);
width: 'width:' ((PIXELSIZE | PERCENTAGE) | CAPITAL_IDENT);
height: 'height:' ((PIXELSIZE | PERCENTAGE) | CAPITAL_IDENT);

stylerule: (LOWER_IDENT | ID_IDENT | CLASS_IDENT)
OPEN_BRACE
(property SEMICOLON)+
CLOSE_BRACE
SEMICOLON;

property: color | background_color | width | height;
variable_assignment: CAPITAL_IDENT ASSIGNMENT_OPERATOR optelling SEMICOLON;



optelling: vermenigvuldiging ((PLUS | MIN) vermenigvuldiging)*;

vermenigvuldiging: element (MUL element)*;

element: PIXELSIZE | PERCENTAGE | CAPITAL_IDENT | COLOR | TRUE | FALSE | '(' optelling ')';

