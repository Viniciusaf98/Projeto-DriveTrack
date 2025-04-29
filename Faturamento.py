import json
import os
from datetime import datetime, timedelta

# Definir o nome da pasta onde os arquivos serão salvos
PASTA_FINANCEIRO = "dados_financeiros"

# Criar a pasta caso ela não exista
if not os.path.exists(PASTA_FINANCEIRO):
    os.makedirs(PASTA_FINANCEIRO)

def obter_data():
    hoje = datetime.now().date()
    resp = input(f"Esses dados correspondem ao dia {hoje.strftime('%d/%m/%Y')}? (S/N): ").strip().upper()
    if resp == "S":
        return hoje
    while True:
        try:
            d, m, a = map(int, input("Digite a data (DD/MM/AAAA): ").split("/"))
            return datetime(a, m, d).date()
        except:
            print("Data inválida. Tente novamente.")

def entrada_float_positiva(msg):
    while True:
        try:
            v = float(input(msg))
            if v < 0:
                print("Informe um valor positivo.")
            else:
                return v
        except:
            print("Entrada inválida. Use ponto para decimais.")

def entrada_int_positiva(msg):
    while True:
        try:
            v = int(input(msg))
            if v < 0:
                print("Informe um número positivo.")
            else:
                return v
        except:
            print("Entrada inválida. Use apenas números inteiros.")

def gerar_feedback(fat):
    if fat >= 200:
        return "🔝 Excelente! Acima da meta, continue assim!"
    if fat >= 150:
        return "✅ Meta batida, bom trabalho!"
    if fat >= 100:
        return "⚠️ Regular, ainda dá pra melhorar."
    return "🚨 Faturamento baixo, tente melhorar amanhã!"

def salvar_dados(data, dados):
    nome = f"financeiro_{data.year}_{data.month:02d}_{data.day:02d}.json"
    caminho = os.path.join(PASTA_FINANCEIRO, nome)
    if os.path.exists(caminho):
        print(f"\n⚠️ Já existia registro para {data.strftime('%d/%m/%Y')}, substituindo.")
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print(f"\n✅ Dados salvos em: {caminho}")

def registrar_novo_dia():
    data = obter_data()
    print("\n🔍 Preenchendo dados do dia...")
    faturamento      = entrada_float_positiva("Faturamento (R$): ")
    combustivel      = entrada_float_positiva("Gasto com combustível (R$): ")
    horas_trabalhadas= entrada_int_positiva("Horas trabalhadas: ")
    corridas         = entrada_int_positiva("Corridas feitas: ")
    km               = entrada_int_positiva("KM rodados: ")

    lucro = faturamento - combustivel
    feedback = gerar_feedback(faturamento)

    # Exibição resumida
    print(f"\n💰 Lucro: R${lucro:.2f} | 📢 {feedback}")

    dados = {
        "data": data.strftime("%d/%m/%Y"),
        "faturamento": faturamento,
        "combustivel": combustivel,
        "horas_trabalhadas": horas_trabalhadas,
        "corridas": corridas,
        "km": km,
        "lucro": lucro,
        "feedback": feedback
    }
    salvar_dados(data, dados)

def listar_arquivos_financeiros():
    return [f for f in os.listdir(PASTA_FINANCEIRO)
            if f.startswith("financeiro_") and f.endswith(".json")]

def extrair_data_do_arquivo(nome):
    try:
        y, m, d = nome.replace("financeiro_", "").replace(".json","").split("_")
        return datetime(int(y), int(m), int(d)).date()
    except:
        return None

def carregar_dados(nome):
    with open(os.path.join(PASTA_FINANCEIRO, nome), encoding="utf-8") as f:
        return json.load(f)

def menu_consulta_dados():
    if not listar_arquivos_financeiros():
        print("\n⚠️ Nenhum registro encontrado ainda.")
        return

    print("\n=== Consulta de Dados ===")
    print("1 - Por dia")
    print("2 - Por semana")
    print("3 - Por mês")
    print("4 - Por ano")
    print("0 - Voltar")
    opc = input("Opção: ").strip()

    # ------------------- Por dia -------------------
# Dentro da função menu_consulta_dados(), substitua o bloco do opc == "1" por isso:

    if opc == "1":
        data = obter_data()
        nome = f"financeiro_{data.year}_{data.month:02d}_{data.day:02d}.json"
        if nome in listar_arquivos_financeiros():
            d = carregar_dados(nome)
            
            # Cálculos auxiliares
            ticket_f = d['faturamento'] / d['corridas'] if d['corridas'] else 0
            ticket_l = d['lucro']        / d['corridas'] if d['corridas'] else 0

            # Impressão formatada
            print(f"\n📆 Dados de {d['data']}:")
            print(f"  • Faturamento:         R${d['faturamento']:.2f}")
            print(f"  • Lucro:               R${d['lucro']:.2f}")
            print(f"  • Corridas realizadas: {d['corridas']}")
            print(f"  • KM rodados:          {d['km']}")
            print(f"  • Ticket médio (R$):   F {ticket_f:.2f} | L {ticket_l:.2f}")
            print(f"  • Feedback:            {d['feedback']}\n")
        else:
            print("❌ Nenhum registro encontrado para esse dia.")


    # ------------------- Por semana -------------------
    elif opc == "2":
        data_ref = obter_data()
        inicio = data_ref - timedelta(days=data_ref.weekday())
        fim    = inicio + timedelta(days=6)

        encontrados = []
        for nome in listar_arquivos_financeiros():
            dt = extrair_data_do_arquivo(nome)
            if dt and inicio <= dt <= fim:
                encontrados.append((dt, carregar_dados(nome)))

        if not encontrados:
            print("❌ Sem registros nessa semana.")
            return

        total_f = total_l = total_corr = total_km = 0
        print(f"\n📅 Semana de {inicio.strftime('%d/%m/%Y')} a {fim.strftime('%d/%m/%Y')}:")
        for dt, d in sorted(encontrados):
            print(f"  • {d['data']}: Faturamento R${d['faturamento']:.2f} | Lucro R${d['lucro']:.2f} | Corridas {d['corridas']} | KM {d['km']}")
            total_f    += d['faturamento']
            total_l    += d['lucro']
            total_corr += d['corridas']
            total_km   += d['km']

        dias = len(encontrados)
        media_f = total_f / dias
        media_l = total_l / dias
        ticket_f = total_f / total_corr if total_corr else 0
        ticket_l = total_l / total_corr if total_corr else 0

        print(f"\n📊 Totais da semana:")
        print(f"    Faturamento: R${total_f:.2f} | Lucro: R${total_l:.2f}")
        print(f"    Corridas: {total_corr} | KM: {total_km}")
        print(f"    Médias/dia — Faturamento: R${media_f:.2f} | Lucro: R${media_l:.2f}")
        print(f"    Ticket médio — Faturamento: R${ticket_f:.2f} | Lucro: R${ticket_l:.2f}")

     # 3. Por mês
    elif opc == "3":
        try:
            m = int(input("Digite o mês (1-12): "))
            a = int(input("Digite o ano (AAAA): "))
        except:
            return print("❌ Entrada inválida.")
        ach = [(extrair_data_do_arquivo(n), n) 
               for n in listar_arquivos_financeiros()
               if (extrair_data_do_arquivo(n).month == m
                   and extrair_data_do_arquivo(n).year == a)]
        if not ach:
            print(f"❌ Sem registros em {m:02d}/{a}.")
        else:
            total_f = total_l = total_corr = total_km = 0
            print(f"\n📅 Mês {m:02d}/{a}:")
            for dt, nome in sorted(ach):
                d = carregar_dados(nome)
                print(f"  • {d['data']}: R${d['faturamento']:.2f} (Lucro R${d['lucro']:.2f})")
                total_f   += d['faturamento']
                total_l   += d['lucro']
                total_corr+= d['corridas']
                total_km  += d['km']
            dias = len(ach)
            print(f"\n📊 Total faturado: R${total_f:.2f} | Lucro: R${total_l:.2f}")
            print(f"    Corridas: {total_corr} | KM: {total_km}")
            print(f"    Médias/dia — Faturamento: R${(total_f/dias):.2f}, KM: {total_km//dias}")

    # ------------------- Por ano -------------------
    elif opc == "4":
        try:
            ano = int(input("Digite o ano (AAAA): "))
        except:
            return print("❌ Ano inválido.")

        encontrados = []
        for nome in listar_arquivos_financeiros():
            dt = extrair_data_do_arquivo(nome)
            if dt and dt.year == ano:
                encontrados.append((dt, carregar_dados(nome)))

        if not encontrados:
            print(f"❌ Sem registros para o ano {ano}.")
            return

        total_f = total_l = total_corr = total_km = 0
        print(f"\n📅 Ano {ano}:")
        for dt, d in sorted(encontrados):
            print(f"  • {d['data']}: Faturamento R${d['faturamento']:.2f} | Lucro R${d['lucro']:.2f} | Corridas {d['corridas']} | KM {d['km']}")
            total_f    += d['faturamento']
            total_l    += d['lucro']
            total_corr += d['corridas']
            total_km   += d['km']

        dias = len(encontrados)
        media_f = total_f / dias
        media_l = total_l / dias
        ticket_f = total_f / total_corr if total_corr else 0
        ticket_l = total_l / total_corr if total_corr else 0

        print(f"\n📊 Totais do ano:")
        print(f"    Faturamento: R${total_f:.2f} | Lucro: R${total_l:.2f}")
        print(f"    Corridas: {total_corr} | KM: {total_km}")
        print(f"    Médias/dia — Faturamento: R${media_f:.2f} | Lucro: R${media_l:.2f}")
        print(f"    Ticket médio — Faturamento: R${ticket_f:.2f} | Lucro: R${ticket_l:.2f}")

    # ------------------- Voltar -------------------
    elif opc == "0":
        return

    else:
        print("❌ Opção inválida.")


def menu():
    while True:
        print("\n=== Controle Financeiro Diário ===")
        print("1 - Registrar novo dia")
        print("2 - Consultar dados (dia, semana, mês ou ano)")
        print("0 - Sair")
        escolha = input("Opção: ").strip()
        if escolha == "1":
            registrar_novo_dia()
        elif escolha == "2":
            menu_consulta_dados()
        elif escolha == "0":
            print("👋 Até mais!")
            break
        else:
            print("❌ Opção inválida.")

# Inicia o programa
menu()
