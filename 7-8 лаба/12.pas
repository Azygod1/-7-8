var
    s: string;
    c, n, d: integer;
begin
    write('Введите строку с цифрами и буквами ');
    readln(s);
    for c := 1 to length(s) do
        if not (s[c] in ['0'..'9']) then begin
            inc(n);
            s[n] := s[c];
        end;
    d := length(s) - n;
    writeln('количество цифр: ', d);
    delete(s, n + 1, d);
    writeln('измененная строка: ', s);
end.