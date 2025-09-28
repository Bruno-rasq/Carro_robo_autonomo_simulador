# Projeto de simulação de Carrinho Robótico.

Este projeto é uma simulação inspirada nos carrinhos robóticos usados em competições de
robótica educacional, especialmente aqueles guiados por faixas pretas em grids (como acontece
em projetos com Arduino e sensores de linha). A ideia principal é criar diferentes modos de
operação para o carrinho dentro de um grid, permitindo tanto controle manual quanto modos
automáticos de navegação.

Até o momento, foi implementado o **modo automático sem direção** (`autoFollow`), no qual o
carrinho segue o caminho disponível no grid sem considerar orientação ou restrições de
movimento. Também foi definida a estrutura básica do projeto, incluindo os modos planejados: -
**Manual**: o usuário controla o carrinho pelo teclado. - **Automático sem direção**: segue as
células acessíveis até o final (já implementado). - **Automático com direção**: segue o caminho
automaticamente, mas com limitações de movimentos (ainda não implementado).

## Desafios e Melhorias Propostos

Nível 1 — Melhorias Básicas
• Interface clara para modos (ex.: enum ou classe Mode).
• Organização da estrutura do grid (classe Grid ou matriz bem 
definida).
• Log de movimentos do carrinho.
• Funções de Reset e Replay.

Nível 2 — Desafios Intermediários
• Detecção de ciclos para evitar loops infinitos.
• Implementar busca de caminhos (BFS, DFS ou A*).
• Obstáculos dinâmicos (inserção/remoção durante execução).
• Velocidade ajustável (simulação de movimento realista).

Nível 3 — Desafios Avançados
• Sensores virtuais simulando visão parcial do carrinho.
• Mapeamento automático (descoberta progressiva do grid).
• Rotas alternativas (escolha do caminho mais curto ou seguro).
• Sistema de energia limitada (bateria com número de passos).

Nível 4 — Extras Criativos
• Modo competição (dois carrinhos correndo no mesmo grid).
• Modo perseguição (um carrinho caça outro).
• Exportar mapa e trajetos (JSON, CSV ou ASCII).
• Visualização gráfica (Tkinter, Pygame ou visualização em terminal).