# ⚡ Exercício Relâmpago Surpresa

## 📚 Tema: Orientação a Objetos

### Edição --- Classe Funcionário 💼

------------------------------------------------------------------------

## 📊 Diagrama de Classe

O diagrama abaixo representa o modelo da classe **Funcionario**,
responsável por calcular o **salário líquido** com base no **salário
bruto**, **acréscimos** e **descontos**.

`<br/>`{=html}
`<img width="780" height="480" alt="Diagrama da Classe Funcionario" src="https://github.com/user-attachments/assets/ab6a1123-5df1-4b3f-bc60-funcionario-diagrama.png" />`{=html}

------------------------------------------------------------------------

## 🧩 O que devo fazer?

Implemente uma classe chamada **Funcionario**, respeitando os princípios
de **encapsulamento**.\
Todos os atributos devem ser **privados** e acessados por meio de
**métodos get e set**.

Crie também um método específico para **calcular o salário líquido**,
conforme a fórmula indicada abaixo.

------------------------------------------------------------------------

## ⚙️ Estrutura da Classe `Funcionario`

### 👨‍💼 Classe `Funcionario`

  -----------------------------------------------------------------------
  Atributo                   Tipo           Descrição
  -------------------------- -------------- -----------------------------
  `nome`                     String         Nome completo do funcionário

  `salarioBruto`             float          Valor do salário bruto

  `totalAcrescimos`          float          Soma de bônus, horas extras e
                                            demais acréscimos

  `totalDescontos`           float          Soma de impostos, atrasos e
                                            demais descontos
  -----------------------------------------------------------------------

------------------------------------------------------------------------

### 🔢 Método

-   `calcularSalarioLiquido()`\
    Calcula o salário líquido conforme a fórmula:

    ``` python
    salário líquido = salário bruto + total acréscimos - total descontos
    ```

    O método deve **retornar o valor do salário líquido**.

------------------------------------------------------------------------

## 💻 Exemplo de Implementação (Python)

``` python
class Funcionario:
    def __init__(self, nome, salarioBruto, totalAcrescimos, totalDescontos):
        self.__nome = nome
        self.__salarioBruto = salarioBruto
        self.__totalAcrescimos = totalAcrescimos
        self.__totalDescontos = totalDescontos

    # Getters e Setters
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome

    def get_salarioBruto(self):
        return self.__salarioBruto
    def set_salarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto

    def get_totalAcrescimos(self):
        return self.__totalAcrescimos
    def set_totalAcrescimos(self, totalAcrescimos):
        self.__totalAcrescimos = totalAcrescimos

    def get_totalDescontos(self):
        return self.__totalDescontos
    def set_totalDescontos(self, totalDescontos):
        self.__totalDescontos = totalDescontos

    # Método principal
    def calcularSalarioLiquido(self):
        return self.__salarioBruto + self.__totalAcrescimos - self.__totalDescontos


# Teste
func = Funcionario("Ana", 5000, 500, 300)
print(f"Funcionário: {func.get_nome()}")
print(f"Salário Líquido: R$ {func.calcularSalarioLiquido():.2f}")
```

------------------------------------------------------------------------

## 📅 Entrega

🕓 **Imediata!**\
Quanto mais demorar, mais o professor ficará chateado com você 😅

📦 **Forma de Entrega:**\
De qualquer jeito --- e-mail, portal, WhatsApp, sinal de fumaça ou
motoboy ---\
mas **deve estar postado na tarefa do portal**.

------------------------------------------------------------------------

## 🏆 Pontuação

  Critério                                      Pontos
  --------------------------------------------- ----------
  Classe criada corretamente                    ✅ 3 pts
  Encapsulamento aplicado                       ✅ 2 pts
  Método `calcularSalarioLiquido()` funcional   ✅ 3 pts
  Teste executável e legível                    ✅ 2 pts

🟥 **Atraso = perda de pontos!**

------------------------------------------------------------------------

## ❓ Dúvidas Frequentes

**1️⃣ Pode fazer em dupla?**\
Sim, em dupla. Vocês e Deus.

**2️⃣ Tem que ser a caneta ou lápis?**\
Não, é código. 😆

**3️⃣ Pode consultar?**\
Pode! Você está em casa, não tem como o professor saber.

**4️⃣ E os exercícios 1 e 2?**\
Era só pra ver se você estava prestando atenção 👀

------------------------------------------------------------------------

## 🧠 Objetivo

Treinar: - **Encapsulamento** - **Construtores** - **Métodos de
cálculo** - **Testes básicos de classe**

------------------------------------------------------------------------

## 🎯 Observação Final

Pode parecer brincadeira...\
Mas **eu nunca brinco!** 😤
