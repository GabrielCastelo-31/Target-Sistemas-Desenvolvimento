# Questões Target-Sistemas-Desenvolvimento

1. Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

    IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

    **RESPOSTA: [Fibonacci](https://github.com/GabrielCastelo-31/Target-Sistemas-Desenvolvimento/blob/main/fibonacci.py])**

2. Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

    IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

    **RESPOSTA: [String_Count](https://github.com/GabrielCastelo-31/Target-Sistemas-Desenvolvimento/blob/main/string_count.py)**

3. Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

    Ao final do processamento, qual será o valor da variável SOMA?
   
    **RESPOSTA: 77**

5. Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___ **RESPOSTA: 9**

b) 2, 4, 8, 16, 32, 64, ____ **RESPOSTA: 128**

c) 0, 1, 4, 9, 16, 25, 36, ____ **RESPOSTA: 49**

d) 4, 16, 36, 64, ____ **RESPOSTA: 100**

e) 1, 1, 2, 3, 5, 8, ____ **RESPOSTA: 13**

f) 2,10, 12, 16, 17, 18, 19, ____ **RESPOSTA: 200**


7. Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

     **RESPOSTA:**
     De acordo com a formulação da pergunta, é preciso realizar as seguintes considerações:
   1. _"Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes."_ e _"usando apenas duas idas até uma das salas das lâmpadas"_. Essas duas frases implicam que **há três salas com uma lâmpada em cada, sendo que podemos visitar no máximo duas delas.**
   2. As lampâdas em questão aquecem o suficente para ser notado pelo tato humano ou aparelhos de medição de temperatura? **Iremos considerar que sim.**
  
   Tendo isso mente podemos descobrir qual interruptor controla cada lâmpada com o seguinte algoritmo:
   1. Acendemos o 1º interruptor por alguns minutos, tempo o suficiente para a lâmpada esquentar. Após isso desligamos e acendemos o segundo interruptor.
   2. Primeira Ida:
      - Vamos a uma das salas e verifiquemos o seguinte:
          - Caso a lâmpada esteja apagada e quente, é controlada pelo **1º interruptor.**
          -  Caso a lâmpada esteja acesa, é controlada pelo **2º interruptor.**
          -   Caso a lâmpada esteja apagada e fria, é controlada pelo **3º interruptor.**
    3. Segunda Ida:
      1. **Caso tenhamos descoberto a lâmpada do 1º interruptor, faremos o seguinte:**
        
            - Iremos a uma outra sala. Caso a lampâda esteja acesa, é controlada pelo 2º interruptor e por exclusão a outra sala é controlada pelo 3º. Caso esteja apagada e fria é controlada pelo 3º interruptor e por exclusão a outra sala é controlada pelo 2º.
        
      2. **Caso tenhamos descoberto a lâmpada do 2º interruptor na primeira ida:**
          
            - Iremos a uma outra sala.  Caso a lampâda esteja apagada e quente, é controlada pelo 1º interruptor e por exclusão a outra sala é controlada pelo 3º. Caso esteja apagada e fria  é controlada pelo 3º interruptor e por exclusão a outra sala é controlada pelo 1º.
