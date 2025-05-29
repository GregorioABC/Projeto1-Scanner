# Projeto 1 – Scanner (Analisador Léxico)

Este projeto implementa um **scanner (analisador léxico)** em Python, seguindo o método descrito no documento `How-To-Make.pdf`. O objetivo é identificar tokens válidos, ignorar comentários e detectar erros léxicos em um arquivo-fonte.

---

## 🎯 Objetivos

- Ler caractere a caractere de um arquivo de entrada.
- Reconhecer tokens válidos da linguagem.
- Exibir erros léxicos com linha e coluna.
- Informar sucesso na análise léxica ao final da leitura.

---

## 🧠 Tokens reconhecidos

- **Palavras reservadas**: `main`, `int`, `float`, `char`, `if`, `else`, `while`, `do`, `for`
- **Identificadores**: letras, dígitos e `_`, começando com letra ou `_`
- **Constantes**:
  - Inteiras: `123`
  - Reais: `12.45`
  - Caracteres: `'a'`, `'9'`
- **Operadores Aritméticos**: `+`, `-`, `*`, `/`
- **Operadores Relacionais**: `<`, `<=`, `>`, `>=`, `==`, `!=`
- **Marcadores**: `(`, `)`, `{`, `}`, `,`, `;`
- **Comentários**:
  - Linha: `// comentário`
  - Bloco: `/* comentário */`
- **Fim de arquivo**: `EOF`
- **Erros Léxicos**:
  - Caracter inválido
  - `!` isolado
  - Constante de caractere mal formada
  - Float mal formado
  - Comentário de bloco não encerrado

---

## 📚 Baseado em
Documento: How-To-Make.pdf

Autor: Lucas Rodolfo C. de Farias (UFPE)
