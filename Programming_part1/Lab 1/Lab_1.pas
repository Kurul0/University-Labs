PROGRAM TEST (INPUT, OUTPUT);
VAR
    S, I, N : INTEGER;
BEGIN
    WRITE ('ВВЕДІТЬ N:');
    READLN (N);
    S := 0;
    FOR I := 1 TO N DO
    BEGIN
        IF I MOD 2 = 0 THEN
            BEGIN
                S := S+I;
                WRITELN ('ПОТОЧНЕ ЗНАЧЕННЯ I=', I, 'S=', S);
            END;
        END;
        WRITELN ('ФІНАЛЬНИЙ РЕЗУЛЬТАТ СУМА S=', S);
    END.