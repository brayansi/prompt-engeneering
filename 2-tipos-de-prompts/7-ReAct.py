from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
msg1 = """
Você é um engenheiro backend Go ajudando a depurar uma REST API.
Use o raciocínio no estilo ReAct: alterne entre "Pensamento:" (seu raciocínio) e "Ação:" (um passo concreto ou verificação que você realizaria).
Após cada ação, escreva "Observação:" com o que você encontrou.
Ao final, conclua com "Resposta Final:" com a correção recomendada.

Não invente informações que não estejam no contexto. Exemplo: se o contexto não fornece logs de erro, não os utilize no seu raciocínio.

Contexto: Um usuário relata que o endpoint `POST /products` sempre retorna HTTP 500.

Aqui está o código do handler para `POST /products`:

```go
func CreateProduct(w http.ResponseWriter, r *http.Request) {
    var product Product
    err := json.NewDecoder(r.Body).Decode(&product)
    if err != nil {
        http.Error(w, "Bad Request", http.StatusBadRequest)
        return
    }

    stmt, err := db.Prepare("INSERT INTO products (id, name, description, price, stock) VALUES (?, ?, ?, ?, ?)")
    if err != nil {
        log.Fatal(err)
    }

    _, err = stmt.Exec(product.ID, product.Name, product.Description, product.Price, product.Stock)
    if err != nil {
        log.Println("Error during Exec:", err)
        http.Error(w, "Internal Server Error", http.StatusInternalServerError)
        return
    }

    w.WriteHeader(http.StatusCreated)
}

type Product struct {
    ID          string  `json:"id"`
    Name        string  `json:"name"`
    Description string  `json:"description"`
    Price       string  `json:"price"` 
    Stock       int     `json:"stock"`
}
```
"""

msg2 = f"""
Você é um planejador de viagens ajudando uma família a escolher a melhor forma de ir de Orlando a Nova York no próximo mês.
Use o raciocínio no estilo ReAct: alterne entre "Pensamento:" (seu raciocínio) e "Ação:" (um passo como verificar tempo de voo, custos ou conveniência).
Após cada ação, escreva "Observação:" com o que você encontrou.
Ao final, conclua com "Resposta Final:" com sua recomendação.

Contexto:
- A família tem 2 adultos e 2 crianças (5 e 8 anos).
- Orçamento: máximo $1.000 para transporte (sem contar hotel).
- Datas: devem chegar no dia 10 de julho à noite.
- Opções:
  - **Avião**: $220 por pessoa ida e volta, voo de 3 horas, mais $80 em taxas de bagagem no total.
  - **Trem**: $150 por pessoa ida e volta, viagem de 20 horas, com WiFi a bordo e camas disponíveis por $50 extra por pessoa.
  - **Aluguel de carro**: $60/dia, 2 dias de direção em cada sentido (gasolina + pedágios estimados em $250 no total). Crianças ficam agitadas em viagens longas.

Outros detalhes:
- A escola das crianças termina no dia 9 de julho ao meio-dia.
- Os pais preferem não chegar muito cansados, pois têm um casamento de família no dia 11 de julho pela manhã.

Inicie seu raciocínio agora.
"""


# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


# response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)

# print_llm_result(msg1, response1)
print_llm_result(msg2, response2)