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
    //--- PARSER: ---
    stylesheet: (statement)*;
    statement: stylerule | variable_assignment;

    stylerule:
    (LOWER_IDENT | ID_IDENT | CLASS_IDENT)
    OPEN_BRACE
        (property SEMICOLON | if_statement)*
    CLOSE_BRACE;

    variable_assignment: CAPITAL_IDENT ASSIGNMENT_OPERATOR expression SEMICOLON;

    color: 'color:' expression;
    background_color: 'background-color:' expression;
    width: 'width:' expression;
    height: 'height:' expression;

    property: color | background_color | width | height;

    expression: vermenigvuldiging ((PLUS | MIN) vermenigvuldiging)*;

    vermenigvuldiging: element (MUL element)*;

    element: PIXELSIZE | PERCENTAGE | CAPITAL_IDENT | COLOR | TRUE | FALSE | SCALAR | '(' expression ')';

    if_statement:
    IF BOX_BRACKET_OPEN (TRUE | FALSE | CAPITAL_IDENT) BOX_BRACKET_CLOSE OPEN_BRACE
        (property SEMICOLON)*
        (if_statement)*
    CLOSE_BRACE (else_statement)*;

    else_statement:
    ELSE OPEN_BRACE
        (property SEMICOLON)*
        (if_statement)*
    CLOSE_BRACE;

