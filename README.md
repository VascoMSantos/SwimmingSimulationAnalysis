# SwimmingSimulationAnalysis
Simulation of swimming races and analysis through an intuitive dashboard.

## Repository Structure

swim_sim/\
│\
├── db/                            # Base de dados e conexões\
│   ├── connection.py              # Função para ligar à base de dados\
│   └── schema.py                  # Criação e reset das tabelas\
│\
├── models/                        # Modelos de dados (objetos de domínio)\
│   ├── athlete.py                 # Geração de atletas e estrutura\
│   └── event.py                   # Estrutura de provas\
│\
├── simulation/                    # Lógica da simulação de provas\
│   └── simulate_race.py           # Simulação de uma prova (gera resultados)\
│\
├── storage/                       # Inserção e queries na base de dados\
│   ├── insert.py                  # Inserção de dados nas tabelas\
│   └── queries.py                 # Queries analíticas (média, ranking, etc.)\
│\
├── dashboard/                     # Dashboard ou visualizações (ex: Streamlit)\
│   └── app.py                     # Interface para explorar os dados (futuro)\
│\
├── main.py                        # Script principal que orquestra tudo\
│\
├── requirements.txt               # Bibliotecas necessárias (ex: pandas, sqlite)\
├── README.md                      # Descrição do projeto\
└── swim_sim.db                    # Base de dados SQLite gerada\
