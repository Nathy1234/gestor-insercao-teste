"""Dados iniciais dos Indicadores Trimestrais — transcritos dos relatórios
HTML de 2026 ("1º/2º/3º TRIMESTRE 2026 - INSERÇÃO.html"). Usado uma única
vez para popular o banco (ver _ind_garantir_dados_iniciais em app.py).

1º e 2º trimestre: regra antiga (5 indicadores com Ponto Mais), só existem
os números finais — ficam como histórico fechado, sem recálculo.
3º trimestre: regra da calculadora por ocorrência (4 critérios, 90%)."""

# ── Critérios da calculadora (3º trimestre em diante) ─────────────────────────
CRITERIOS_CALCULADORA = [
    {'nome': 'Meta Diária', 'curto': 'Meta Diária', 'peso': 0.20,
     'descricao': 'Inserção de disciplinas ou cursos (completas ou parciais) no Moodle e Inova Carreira, com base nos materiais liberados.'},
    {'nome': 'Acompanhamento das Disciplinas', 'curto': 'Acomp. Disciplinas', 'peso': 0.20,
     'descricao': 'Ajustes solicitados por Curadoria, Revisão ou Coordenação feitos em até 2 dias úteis.'},
    {'nome': 'Taxa de Retorno', 'curto': 'Taxa de Retorno', 'peso': 0.30,
     'descricao': 'Avaliações Integradas de cada módulo (Graduação, DP, ADP) e controle dos retornos das inserções.'},
    {'nome': 'Organização das Ferramentas de Trabalho', 'curto': 'Ferramentas', 'peso': 0.20,
     'descricao': 'Planilhas, Planner e Teams atualizados com o status das demandas.'},
]

EQUIPE_2026 = [
    # nome, função, valor total, supervisão
    ('Natália', 'Supervisão de Inserção', 2000, True),
    ('Junior', 'Inserção', 1500, False),
    ('Stefanye', 'Insersora', 1500, False),
    ('Pedro', 'Insersor', 1500, False),
    ('Felipe', 'Insersor / Curador', 1500, False),
    ('Lucas', 'Insersor', 1500, False),
]

# ── Mudanças de equipe no 4º trimestre de 2026 ──
# Felipe não faz mais parte da equipe a partir do 4º/2026.
SAIRAM_NO_4TRI_2026 = ('Felipe',)
# Natália é gestora até 16/10/2026 (proporcional aos dias, pelo % da equipe
# nesse período). Junior assume a gestão em 17/10, mas no 4º/2026 é calculado
# igual aos demais: R$ 1.500, trimestre inteiro, só pelas próprias ocorrências.
TROCA_GESTAO_4TRI_2026 = {
    'sai': 'Natália', 'assume': 'Junior',
    'ultimo_dia': '2026-10-16', 'primeiro_dia': '2026-10-17',
    'funcao_nova': 'Inserção · gestão a partir de 17/10',
}

# criterio: 0 Meta Diária · 1 Acompanhamento · 2 Taxa de Retorno · 3 Ferramentas
OCORRENCIAS_3TRI_2026 = [
    {'colab': 'Junior', 'criterio': 2, 'data': '2026-07-01', 'grav': 'medio', 'status': 'Ajustado',
     'desc': 'Enunciado duplicado na Atividade 3 — questões 3 e 4.',
     'links': [{'t': 'Teams', 'u': 'https://teams.microsoft.com/l/message/19:e0dfc78024544084b64ffdfe40db4d04@thread.tacv2/1782906483596?tenantId=31ab4bbb-9b15-4ee3-81fe-50bbd2016ce3&groupId=7ce913bd-9cc9-49c7-a5e3-b19349218e76&parentMessageId=1782906483596&teamName=Produ%C3%A7%C3%A3o%20de%20Materiais&channelName=Ajustes%20Internos%20-%20Produ%C3%A7%C3%A3o%20de%20Materiais&createdTime=1782906483596'}]},
    {'colab': 'Felipe', 'criterio': 2, 'data': '2026-07-06', 'grav': 'leve', 'status': 'Ajustado',
     'desc': 'Luiz mandou uma disciplina vigente e a padrão também estava errada. Nathy ajustou: a Atividade de Estudo 01 estava valendo 0,05 — faltou colocar 0,50.',
     'links': [{'t': 'Disciplina vigente', 'u': 'https://www.eadunifatecie.com.br/course/view.php?id=105901'},
               {'t': 'Disciplina padrão', 'u': 'https://www.eadunifatecie.com.br/course/view.php?id=66169'}]},
    {'colab': 'Junior', 'criterio': 2, 'data': '2026-07-06', 'grav': 'medio', 'status': 'Ajustado',
     'desc': 'A atualização das atividades (APA) desta disciplina foi enviada em novembro do ano passado, mas faltou inserir a última parte. Solicitação de Louise Ribeiro (ANTIGA – GRADUAÇÃO | Inserção de Materiais).',
     'links': [{'t': 'Disciplina', 'u': 'https://www.eadunifatecie.com.br/course/view.php?id=36962'},
               {'t': 'Dropbox', 'u': 'https://www.dropbox.com/scl/fo/px0s9kbh1909ojiuyowgd/AIMnqXK4F4dOiye6PRn3sxg/ATIVIDADES/2025?rlkey=n2b09azi0kc6xtujpi53savps&subfolder_nav_tracking=1&st=562m4294&dl=0'}]},
    {'colab': 'Lucas', 'criterio': 2, 'data': '2026-07-22', 'grav': 'alto', 'status': 'Ajustado',
     'desc': 'Inserido APA com respostas — Contabilidade Societária.',
     'links': [{'t': 'Dropbox', 'u': 'https://www.dropbox.com/sh/bmjwop72c5mwquu/AAAYDf8UepMSsFKVfeGyEyDPa?dl=0'}]},
    {'colab': 'Pedro', 'criterio': 2, 'data': '2026-07-23', 'grav': 'alto', 'status': 'Ajustado',
     'desc': 'Nathy ajustou — na disciplina Instalações Elétricas não foram inseridos os materiais da APA (templates e roteiro para o aluno).',
     'links': []},
    {'colab': 'Pedro', 'criterio': 2, 'data': '2026-07-31', 'grav': 'alto', 'status': 'Ajustado',
     'desc': 'Disciplinas liberadas com APA (Clara IA) que não haviam sido liberadas para a parametrização. Entre as 14, duas não foram alteradas na padrão, e veio retorno de disciplina vigente com APA desatualizada.',
     'links': [{'t': 'Teams', 'u': 'https://teams.microsoft.com/l/message/19:50575091ce74432c813d5a1332169f18@thread.tacv2/1780943955256?tenantId=31ab4bbb-9b15-4ee3-81fe-50bbd2016ce3&groupId=7ce913bd-9cc9-49c7-a5e3-b19349218e76&parentMessageId=1780943955256&teamName=Produ%C3%A7%C3%A3o%20de%20Materiais&channelName=Inser%C3%A7%C3%A3o%20de%20Materiais&createdTime=1780943955256&ngc=true'}]},
    {'colab': 'Junior', 'criterio': 0, 'data': '2026-07-31', 'grav': 'medio', 'status': 'Ajustado',
     'desc': 'A disciplina havia sido ajustada nas padrões, mas faltou ajustar a padrão de pós.',
     'links': [{'t': 'Teams', 'u': 'https://teams.microsoft.com/l/message/19:2a60721d-4b23-4fc3-bf53-497cf5efe34c_91be7a8c-cbae-41c1-996c-d374cc101b7b@unq.gbl.spaces/1785504661192?context=%7B%22contextType%22%3A%22chat%22%7D'}]},
    {'colab': 'Pedro', 'criterio': 0, 'data': '2026-08-03', 'grav': 'alto', 'status': '',
     'desc': 'Em 07/07 a Nathy enviou as disciplinas do MEC de Educação Especial; até 03/08 não tinham sido feitas, e só foram realizadas no dia da avaliação do MEC.',
     'links': []},
]

# ── Histórico (regra antiga) ──────────────────────────────────────────────────

_ESCALA_GERAL = '1–3 → 20% · 4–6 → 40% · 7–9 → 50% · 10–12 → 75% · 13+ → 100%'
_ESCALA_PONTO = '1–3 → 0% · 4–7 → 25% · 8–11 → 50% · 12+ → 100%'
_PONTO_DESC = 'Cada colaborador deverá bater o ponto corretamente (entrada, intervalo de almoço, retorno do intervalo, saída). Ocorrências justificáveis são avaliadas individualmente.'

_SHAREPOINT = {'t': 'Planilha Compartilhada com Heider — SharePoint', 'icone': '📊',
               'u': 'https://fatecie-my.sharepoint.com/:x:/g/personal/natalia_araujo_fatecie_edu_br/IQDHCpVecejlSo7r6fNEHRbEAXn360HiUmIKi-nvq248x60?e=1l7erj'}
_NOTA_CLOCKIFY = '⚠️ O Clockify foi iniciado no meio do trimestre. Demandas anteriores constam na planilha.'
_KRONOS = {'t': 'Kronos — Demandas da Equipe', 'icone': '⏱️', 'u': 'https://kronoslabtecie.web.app/i'}
_NOTA_KRONOS = '⚠️ O Kronos foi iniciado no meio do trimestre. Demandas anteriores constam em registros internos.'

def _clockify(user_id, com_projetos=False):
    extra_f = '%22projects%22:%5B%5D,' if com_projetos else ''
    extra_e = ',projects' if com_projetos else ''
    extra_o = '%22projects%22:%7B%22status%22:%22ACTIVE%22%7D,' if com_projetos else ''
    return {'t': 'Clockify — Relatório 1º Trimestre 2026', 'icone': '⏱️',
            'u': ('https://app.clockify.me/reports/summary?start=2026-01-01T00:00:00.000Z&end=2026-03-31T23:59:59.999Z'
                  '&filterValuesData=%7B%22users%22:%5B%22' + user_id + '%22%5D,%22billing%22:%5B%22BILLABLE%22,%22NOT_BILLABLE%22%5D,'
                  '%22break%22:%5B%22BREAK%22,%22REGULAR%22%5D,%22invoicing%22:%5B%22INVOICED%22,%22UNINVOICED%22%5D,'
                  '%22userAndGroup%22:%5B%5D,%22tags%22:%5B%5D,' + extra_f + '%22statuses%22:%5B%5D%7D&exclude=tags' + extra_e +
                  '&filterOptions=%7B%22userAndGroup%22:%7B%22status%22:%22ACTIVE_WITH_PENDING%22%7D,%22tags%22:%7B%22status%22:%22ACTIVE%22,%22contains%22:%22CONTAINS%22%7D,'
                  + extra_o + '%22statuses%22:%7B%22status%22:%22ACTIVE%22%7D%7D')}

def _ind(nome, ref, pct, resultado, cls):
    return {'nome': nome, 'ref': ref, 'pct': pct, 'resultado': resultado, 'cls': cls}

def _info(label, val, cls):
    return {'label': label, 'val': val, 'cls': cls}

HISTORICO_1TRI_2026 = {
    'meses': ['Jan', 'Fev', 'Mar'],
    'subtitulo': 'Janeiro, Fevereiro e Março',
    'pct_equipe': '95,8%', 'pct_equipe_num': 95.8,
    'pct_equipe_desc': 'Média consolidada de todos os indicadores dos colaboradores no trimestre. O valor representa o percentual atingido sobre a meta de 100%.',
    'cards': [
        {'label': 'Colaboradores', 'valor': '5', 'sub': 'Supervisão, Inserção e Curadoria', 'cor': 'green'},
        {'label': 'Demandas Totais', 'valor': '1.286+', 'sub': 'Disciplinas e demandas realizadas', 'cor': 'blue'},
        {'label': 'Meta Individual Média', 'valor': 'R$ 1.525', 'sub': 'Média dos valores finais atingidos', 'cor': 'orange'},
        {'label': 'Metas 100% Atingidas', 'valor': '3 / 5', 'sub': 'Stefanye, Natalia (meta) e Felipe', 'cor': 'green'},
    ],
    'tem_demandas': False,
    'nota_colaboradores': 'Os dados de Fevereiro e Março para disciplinas inseridas ainda estão sendo consolidados nas abas mensais da planilha. Os totais de demandas representam o acumulado disponível até o fechamento do trimestre.',
    'escalas': True,
    'criterios_nota': 'Cada colaborador é avaliado em 5 indicadores. O peso de cada um define quanto ele representa no valor total da meta. As ocorrências registradas no trimestre determinam o percentual de desconto aplicado.',
    'grupos_criterios': [
        {'titulo': 'Indicadores — Insersores (Junior, Stefanye, Pedro)', 'secao': 'Meta — Insersores', 'icone': '📋', 'itens': [
            {'titulo': 'Ponto Mais', 'desc': _PONTO_DESC, 'escala': _ESCALA_PONTO, 'peso': '20%'},
            {'titulo': 'Meta Diária', 'desc': 'Inserção de disciplinas ou cursos completas ou parciais nas plataformas Moodle e Inova Carreira, com base em materiais liberados.', 'escala': _ESCALA_GERAL, 'peso': '20%'},
            {'titulo': 'Acompanhamento das Disciplinas', 'desc': 'Realização dos ajustes solicitados por Curadoria, Revisão ou Coordenação no prazo de até 2 dias úteis. Organização das Avaliações Integradas de cada módulo (Graduação, DP, ADP) e Plataformas.', 'escala': _ESCALA_GERAL, 'peso': '20%'},
            {'titulo': 'Taxa de Retorno', 'desc': 'Taxa de retorno das disciplinas inseridas ou outras demandas da inserção de materiais. Em caso de retorno, analisar a quantidade e o nível da irregularidade.', 'escala': _ESCALA_GERAL, 'peso': '30%'},
            {'titulo': 'Organização das Ferramentas de Trabalho', 'desc': 'Atualização e organização das ferramentas de controle (planilhas, Planner, Teams) com status das demandas.', 'escala': _ESCALA_GERAL, 'peso': '10%'},
        ]},
        {'titulo': 'Indicadores — Curadores (Felipe)', 'secao': 'Meta — Curadores', 'icone': '🔍', 'itens': [
            {'titulo': 'Ponto Mais', 'desc': _PONTO_DESC, 'escala': _ESCALA_PONTO, 'peso': '20%'},
            {'titulo': 'Meta Diária', 'desc': 'Análise técnica e pedagógica das disciplinas inseridas no Moodle e Inova Carreira, com retorno em até 5 dias úteis. Acompanhamento diário.', 'escala': _ESCALA_GERAL, 'peso': '20%'},
            {'titulo': 'Acompanhamento Conclusão de Disciplinas', 'desc': 'Validação e liberação das disciplinas com pelo menos 7 dias de antecedência da publicação do módulo. Periodicidade mensal/trimestral.', 'escala': _ESCALA_GERAL, 'peso': '20%'},
            {'titulo': 'Taxa de Retorno', 'desc': 'Controle de qualidade com taxa de ajustes inferior a 40% das demandas atribuídas no trimestre. Periodicidade mensal/trimestral.', 'escala': _ESCALA_GERAL, 'peso': '30%'},
            {'titulo': 'Organização das Ferramentas de Trabalho', 'desc': 'Registro e acompanhamento das solicitações no Planner, TEAMS e TRELLO, com visibilidade e rastreabilidade. Periodicidade mensal/trimestral.', 'escala': _ESCALA_GERAL, 'peso': '10%'},
        ]},
        {'titulo': 'Indicadores — Supervisão (Natália)', 'secao': 'Meta — Supervisão de Inserção', 'icone': '👑', 'itens': [
            {'titulo': 'Ponto Mais', 'desc': _PONTO_DESC, 'escala': _ESCALA_PONTO, 'peso': '20%'},
            {'titulo': 'Meta Diária — Alinhamento de Equipes', 'desc': 'Garantia de alinhamento entre as equipes de Inserção, indicadores, Curadoria e Revisão, evitando atrasos na publicação. Acompanhamento diário.', 'escala': _ESCALA_GERAL, 'peso': '20%'},
            {'titulo': 'Acompanhamento da Equipe', 'desc': 'Acompanhamento da execução e indicadores de desempenho da equipe de Inserção, realizando feedbacks mensais e auxílio individual e coletivo. Periodicidade mensal/trimestral.', 'escala': _ESCALA_GERAL, 'peso': '20%'},
            {'titulo': 'Taxa de Retorno / Planejamento', 'desc': 'Planejamento e organização das disciplinas inseridas no módulo, garantindo entrega com antecedência. Acompanhamento diário, mensal e trimestral.', 'escala': _ESCALA_GERAL, 'peso': '30%'},
            {'titulo': 'Organização das Ferramentas de Trabalho', 'desc': 'Garantir que todas as inserções (disciplinas, avaliações e cursos) estejam completas antes da data de abertura e todas as ferramentas estejam atualizadas e organizadas.', 'escala': _ESCALA_GERAL, 'peso': '10%'},
        ]},
    ],
    'participantes': [
        {'nome': 'Natália', 'funcao': 'Supervisão de Inserção', 'funcao_curta': 'Supervisão', 'valor_total': 2000, 'supervisao': True,
         'pct': '95%', 'pct_cls': 'warn', 'valor_final': 'R$ 1.816', 'status': 'Quase lá', 'status_cls': 'warn',
         'meses': ['100%', '106,4%', '121,3%'],
         'indicadores': [_ind('1. Ponto Mais', 'R$ 400 · Peso 20%', '75%', 'R$ 300', 'warn'),
                         _ind('2. Meta Diária', 'R$ 400 · Peso 20%', '100%', 'R$ 400', 'ok'),
                         _ind('3. Acomp. Disciplinas', 'R$ 400 · Peso 20%', '100%', 'R$ 400', 'ok'),
                         _ind('4. Taxa de Retorno', 'R$ 600 · Peso 30%', '100%', 'R$ 600', 'ok'),
                         _ind('5. Ferramentas', 'R$ 200 · Peso 10%', '100%', 'R$ 200', 'ok')],
         'infos': [_info('Total Final', 'R$ 1.816 / 2.000', 'warn'), _info('Erros / Retornos', '0 erros · 0 retornos', 'ok'),
                   _info('Ponto Mais — Ocorrências', '5 ocorrências de ponto', 'warn'), _info('Desconto Equipe', 'R$ 84 (5,42%)', 'warn')],
         'links': [_clockify('69960ae3afc0047f7209d39b'), _SHAREPOINT], 'nota_links': _NOTA_CLOCKIFY},
        {'nome': 'Junior', 'funcao': 'Inserção', 'funcao_curta': 'Inserção', 'valor_total': 1500, 'supervisao': False,
         'pct': '96%', 'pct_cls': 'warn', 'valor_final': 'R$ 1.410', 'status': 'Quase lá', 'status_cls': 'warn',
         'meses': ['101,2%', '100%', '100,8%'],
         'indicadores': [_ind('1. Ponto Mais', 'R$ 300 · Peso 20%', '100%', 'R$ 300', 'ok'),
                         _ind('2. Meta Diária', 'R$ 300 · Peso 20%', '100%', 'R$ 300', 'ok'),
                         _ind('3. Acomp. Disciplinas', 'R$ 300 · Peso 20%', '100%', 'R$ 300', 'ok'),
                         _ind('4. Taxa de Retorno', 'R$ 450 · Peso 30%', '80%', 'R$ 360', 'warn'),
                         _ind('5. Ferramentas', 'R$ 150 · Peso 10%', '100%', 'R$ 150', 'ok')],
         'infos': [_info('Total Final', 'R$ 1.410 / 1.500', 'warn'), _info('Retorno Erros', '1 erro geral · 2 retornos curadoria', 'warn')],
         'links': [_clockify('69962be7afc0047f720da0b8'), _SHAREPOINT], 'nota_links': _NOTA_CLOCKIFY},
        {'nome': 'Stefanye', 'funcao': 'Insersora', 'funcao_curta': 'Insersora', 'valor_total': 1500, 'supervisao': False,
         'pct': '100%', 'pct_cls': 'ok', 'valor_final': 'R$ 1.500', 'status': 'Meta atingida', 'status_cls': 'ok',
         'meses': ['101,1%', '100%', '100,1%'],
         'indicadores': [_ind('1. Ponto Mais', 'R$ 300 · Peso 20%', '100%', 'R$ 300', 'ok'),
                         _ind('2. Meta Diária', 'R$ 300 · Peso 20%', '100%', 'R$ 300', 'ok'),
                         _ind('3. Acomp. Disciplinas', 'R$ 300 · Peso 20%', '100%', 'R$ 300', 'ok'),
                         _ind('4. Taxa de Retorno', 'R$ 450 · Peso 30%', '100%', 'R$ 450', 'ok'),
                         _ind('5. Ferramentas', 'R$ 150 · Peso 10%', '100%', 'R$ 150', 'ok')],
         'infos': [_info('Total Final', 'R$ 1.500 / 1.500 ✓', 'ok'), _info('Erros / Retornos', '0 erros · 0 retornos', 'ok'),
                   _info('Ponto Mais — Ocorrências', '2 ocorrências de ponto (jan)', 'warn')],
         'links': [_clockify('69984c380168d224060fe251', True), _SHAREPOINT], 'nota_links': _NOTA_CLOCKIFY},
        {'nome': 'Pedro', 'funcao': 'Insersor', 'funcao_curta': 'Insersor', 'valor_total': 1500, 'supervisao': False,
         'pct': '88%', 'pct_cls': 'bad', 'valor_final': 'R$ 1.380', 'status': 'Atenção', 'status_cls': 'bad',
         'meses': ['101,2%', '100%', '105,2%'],
         'indicadores': [_ind('1. Ponto Mais', 'R$ 300 · Peso 20%', '100%', 'R$ 300', 'ok'),
                         _ind('2. Meta Diária', 'R$ 300 · Peso 20%', '100%', 'R$ 300', 'ok'),
                         _ind('3. Acomp. Disciplinas', 'R$ 300 · Peso 20%', '80%', 'R$ 240', 'warn'),
                         _ind('4. Taxa de Retorno', 'R$ 450 · Peso 30%', '100%', 'R$ 450', 'ok'),
                         _ind('5. Ferramentas', 'R$ 150 · Peso 10%', '60%', 'R$ 90', 'bad')],
         'infos': [_info('Total Final', 'R$ 1.380 / 1.500', 'bad'), _info('Retorno Erros', '5 erros gerais · 0 retornos curadoria', 'warn'),
                   _info('Pontos de Atenção', 'Acomp. Disciplinas e Ferramentas', 'bad')],
         'links': [_clockify('699d9949667a5341a6407bf2', True), _SHAREPOINT], 'nota_links': _NOTA_CLOCKIFY},
        {'nome': 'Felipe', 'funcao': 'Insersor / Curador', 'funcao_curta': 'Insersor / Curador', 'valor_total': 1500, 'supervisao': False,
         'pct': '100%', 'pct_cls': 'ok', 'valor_final': 'R$ 1.500', 'status': 'Meta atingida', 'status_cls': 'ok',
         'meses': ['100%', '100%', '100%'],
         'indicadores': [_ind('1. Ponto Mais', 'R$ 300 · Peso 20%', '100%', 'R$ 300', 'ok'),
                         _ind('2. Meta Diária', 'R$ 300 · Peso 20%', '100%', 'R$ 300', 'ok'),
                         _ind('3. Taxa de Retorno', 'R$ 300 · Peso 20%', '100%', 'R$ 300', 'ok'),
                         _ind('4. Acomp. Disciplinas', 'R$ 450 · Peso 30%', '100%', 'R$ 450', 'ok'),
                         _ind('5. Ferramentas', 'R$ 150 · Peso 10%', '100%', 'R$ 150', 'ok')],
         'infos': [_info('Total Final', 'R$ 1.500 / 1.500 ✓', 'ok'), _info('Erros / Retornos', '0 erros · 0 retornos', 'ok'),
                   _info('Ponto Mais — Ocorrências', '2 ocorrências de ponto (jan)', 'warn')],
         'links': [_clockify('699d9949667a5341a6407bf3', True), _SHAREPOINT], 'nota_links': _NOTA_CLOCKIFY},
    ],
}

HISTORICO_2TRI_2026 = {
    'meses': ['Abr', 'Mai', 'Jun'],
    'subtitulo': 'Abril, Maio e Junho',
    'pct_equipe': '95,7%', 'pct_equipe_num': 95.7,
    'pct_equipe_desc': 'Média consolidada de todos os colaboradores no trimestre. O valor representa o percentual atingido sobre a meta total da equipe.',
    'cards': [
        {'label': 'Colaboradores', 'valor': '6', 'sub': 'Supervisão, Inserção e Curadoria', 'cor': 'green'},
        {'label': 'Demandas Totais', 'valor': '2.839', 'sub': 'Total acumulado da equipe', 'cor': 'blue'},
        {'label': 'Total Equipe', 'valor': 'R$ 7.858', 'sub': 'Soma dos totais finais', 'cor': 'orange'},
        {'label': 'Metas 100% Atingidas', 'valor': '3 / 6', 'sub': 'Junior, Stefanye e Lucas', 'cor': 'green'},
    ],
    'tem_demandas': True,
    'nota_colaboradores': 'Lucas integrou a equipe neste trimestre com meta proporcional de R$ 1.252,74 baseada no período de atuação.',
    'escalas': True,
    'criterios_nota': 'Cada colaborador é avaliado em 5 indicadores. O peso de cada um define quanto ele representa no valor total da meta.',
    'grupos_criterios': [
        {'titulo': 'Critérios aplicados a todos os colaboradores', 'secao': 'Indicadores da Equipe', 'icone': '📋', 'itens': [
            {'titulo': 'Ponto Mais', 'desc': 'Cumprimento correto dos registros de entrada e saída no sistema de ponto. Ocorrências justificáveis são avaliadas individualmente.', 'escala': _ESCALA_PONTO, 'peso': '20%'},
            {'titulo': 'Meta Diária', 'desc': 'Inserção de disciplinas ou cursos completas ou parciais nas plataformas Moodle e Inova Carreira, com base em materiais liberados.', 'escala': _ESCALA_GERAL, 'peso': '20%'},
            {'titulo': 'Acompanhamento das Disciplinas', 'desc': 'Realização dos ajustes solicitados por Curadoria, Revisão ou Coordenação no prazo de até 2 dias úteis. Taxa de retorno.', 'escala': _ESCALA_GERAL, 'peso': '20%'},
            {'titulo': 'Taxa de Retorno', 'desc': 'Organização das Avaliações Integradas de cada módulo (Graduação, DP, ADP) e controle da taxa de retornos das inserções.', 'escala': _ESCALA_GERAL, 'peso': '30%'},
            {'titulo': 'Organização das Ferramentas de Trabalho', 'desc': 'Atualização e organização das ferramentas de controle (planilhas, Planner, Teams) com status das demandas.', 'escala': _ESCALA_GERAL, 'peso': '10%'},
        ]},
    ],
    'participantes': [
        {'nome': 'Natália', 'funcao': 'Supervisão de Inserção', 'funcao_curta': 'Supervisão', 'valor_total': 2000, 'supervisao': True,
         'pct': '91,8%', 'pct_cls': 'warn', 'valor_final': 'R$ 1.836,86', 'demandas': '514', 'status': 'Quase lá', 'status_cls': 'warn',
         'meses': ['126,4%', '132,5%', '117,9%'],
         'indicadores': [_ind('1. Ponto Mais', 'R$ 400,00 · Peso 20%', '75%', 'R$ 320,00', 'bad'),
                         _ind('2. Meta Diária', 'R$ 400,00 · Peso 20%', '100%', 'R$ 400,00', 'ok'),
                         _ind('3. Acomp. Disciplinas', 'R$ 400,00 · Peso 20%', '100%', 'R$ 400,00', 'ok'),
                         _ind('4. Taxa de Retorno', 'R$ 600,00 · Peso 30%', '100%', 'R$ 600,00', 'ok'),
                         _ind('5. Ferramentas', 'R$ 200,00 · Peso 10%', '100%', 'R$ 200,00', 'ok')],
         'infos': [_info('Total Final', 'R$ 1.836,86 / 2.000 — 91,8%', 'warn'), _info('Erros / Retornos', '1 erro geral (abr)', 'warn'),
                   _info('Ponto Mais — Ocorrências', '4 ocorrências (abr+mai)', 'warn'),
                   _info('Desconto Equipe', 'R$ 83,14 descontados (% equipe: 95,67%)', 'warn')],
         'links': [_KRONOS], 'nota_links': _NOTA_KRONOS},
        {'nome': 'Junior', 'funcao': 'Inserção', 'funcao_curta': 'Inserção', 'valor_total': 1500, 'supervisao': False,
         'pct': '100%', 'pct_cls': 'ok', 'valor_final': 'R$ 1.500', 'demandas': '459', 'status': 'Meta atingida', 'status_cls': 'ok',
         'meses': ['100,0%', '100,8%', '100,3%'],
         'indicadores': [_ind('1. Ponto Mais', 'R$ 300,00 · Peso 20%', '100%', 'R$ 300,00', 'ok'),
                         _ind('2. Meta Diária', 'R$ 300,00 · Peso 20%', '100%', 'R$ 300,00', 'ok'),
                         _ind('3. Acomp. Disciplinas', 'R$ 300,00 · Peso 20%', '100%', 'R$ 300,00', 'ok'),
                         _ind('4. Taxa de Retorno', 'R$ 450,00 · Peso 30%', '100%', 'R$ 450,00', 'ok'),
                         _ind('5. Ferramentas', 'R$ 150,00 · Peso 10%', '100%', 'R$ 150,00', 'ok')],
         'infos': [_info('Total Final', 'R$ 1.500 / 1.500 ✓ — 100%', 'ok'), _info('Erros / Retornos', '1 retorno curadoria (abr)', 'warn'),
                   _info('Ponto Mais — Ocorrências', '0 ocorrências', 'ok')],
         'links': [_KRONOS], 'nota_links': _NOTA_KRONOS},
        {'nome': 'Stefanye', 'funcao': 'Insersora', 'funcao_curta': 'Insersora', 'valor_total': 1500, 'supervisao': False,
         'pct': '100%', 'pct_cls': 'ok', 'valor_final': 'R$ 1.500', 'demandas': '619', 'status': 'Meta atingida', 'status_cls': 'ok',
         'meses': ['105,5%', '109,4%', '104,5%'],
         'indicadores': [_ind('1. Ponto Mais', 'R$ 300,00 · Peso 20%', '100%', 'R$ 300,00', 'ok'),
                         _ind('2. Meta Diária', 'R$ 300,00 · Peso 20%', '100%', 'R$ 300,00', 'ok'),
                         _ind('3. Acomp. Disciplinas', 'R$ 300,00 · Peso 20%', '100%', 'R$ 300,00', 'ok'),
                         _ind('4. Taxa de Retorno', 'R$ 450,00 · Peso 30%', '100%', 'R$ 450,00', 'ok'),
                         _ind('5. Ferramentas', 'R$ 150,00 · Peso 10%', '100%', 'R$ 150,00', 'ok')],
         'infos': [_info('Total Final', 'R$ 1.500 / 1.500 ✓ — 100%', 'ok'), _info('Erros / Retornos', '0 erros · 0 retornos', 'ok'),
                   _info('Ponto Mais — Ocorrências', '0 ocorrências', 'ok')],
         'links': [_KRONOS], 'nota_links': _NOTA_KRONOS},
        {'nome': 'Pedro', 'funcao': 'Insersor', 'funcao_curta': 'Insersor', 'valor_total': 1500, 'supervisao': False,
         'pct': '90%', 'pct_cls': 'bad', 'valor_final': 'R$ 1.350', 'demandas': '601', 'status': 'Atenção', 'status_cls': 'bad',
         'meses': ['100,8%', '101,2%', '101,3%'],
         'indicadores': [_ind('1. Ponto Mais', 'R$ 300,00 · Peso 20%', '100%', 'R$ 300,00', 'ok'),
                         _ind('2. Meta Diária', 'R$ 300,00 · Peso 20%', '80%', 'R$ 240,00', 'warn'),
                         _ind('3. Acomp. Disciplinas', 'R$ 300,00 · Peso 20%', '80%', 'R$ 300,00', 'warn'),
                         _ind('4. Taxa de Retorno', 'R$ 450,00 · Peso 30%', '80%', 'R$ 360,00', 'warn'),
                         _ind('5. Ferramentas', 'R$ 150,00 · Peso 10%', '100%', 'R$ 150,00', 'ok')],
         'infos': [_info('Total Final', 'R$ 1.350 / 1.500 — 90%', 'bad'), _info('Erros / Retornos', '5 erros · 3 ret. curadoria (abr)', 'warn'),
                   _info('Pontos de Atenção', 'Meta Diária, Acomp. e Taxa Retorno', 'bad')],
         'links': [_KRONOS], 'nota_links': _NOTA_KRONOS},
        {'nome': 'Felipe', 'funcao': 'Insersor / Curador', 'funcao_curta': 'Insersor / Curador', 'valor_total': 1500, 'supervisao': False,
         'pct': '89%', 'pct_cls': 'bad', 'valor_final': 'R$ 1.335', 'demandas': '284', 'status': 'Quase lá', 'status_cls': 'warn',
         'meses': ['100,2%', '101,7%', '100,3%'],
         'indicadores': [_ind('1. Ponto Mais', 'R$ 300,00 · Peso 20%', '75%', 'R$ 225,00', 'bad'),
                         _ind('2. Meta Diária', 'R$ 300,00 · Peso 20%', '100%', 'R$ 300,00', 'ok'),
                         _ind('3. Acomp. Disciplinas', 'R$ 300,00 · Peso 20%', '100%', 'R$ 300,00', 'ok'),
                         _ind('4. Taxa de Retorno', 'R$ 450,00 · Peso 30%', '80%', 'R$ 360,00', 'warn'),
                         _ind('5. Ferramentas', 'R$ 150,00 · Peso 10%', '100%', 'R$ 150,00', 'ok')],
         'infos': [_info('Total Final', 'R$ 1.335 / 1.500 — 89%', 'warn'), _info('Erros / Retornos', '0 erros · 0 retornos', 'ok'),
                   _info('Ponto Mais — Ocorrências', '4 ocorrências (abr+jun)', 'warn')],
         'links': [_KRONOS], 'nota_links': _NOTA_KRONOS},
        {'nome': 'Lucas', 'funcao': 'Insersor', 'funcao_curta': 'Insersor', 'valor_total': 1252.74, 'supervisao': False,
         'pct': '100%', 'pct_cls': 'ok', 'valor_final': 'R$ 1.252,74', 'demandas': '362', 'status': 'Meta atingida', 'status_cls': 'ok',
         'meses': ['100,6%', '102,9%', '102,4%'],
         'indicadores': [_ind('1. Ponto Mais', 'R$ 250,55 · Peso 20%', '100%', 'R$ 250,55', 'ok'),
                         _ind('2. Meta Diária', 'R$ 250,55 · Peso 20%', '100%', 'R$ 250,55', 'ok'),
                         _ind('3. Acomp. Disciplinas', 'R$ 250,55 · Peso 20%', '100%', 'R$ 250,55', 'ok'),
                         _ind('4. Taxa de Retorno', 'R$ 375,82 · Peso 30%', '100%', 'R$ 375,82', 'ok'),
                         _ind('5. Ferramentas', 'R$ 125,27 · Peso 10%', '100%', 'R$ 125,27', 'ok')],
         'infos': [_info('Total Final', 'R$ 1.252,74 / 1.252,74 ✓ — 100%', 'ok'), _info('Erros / Retornos', '1 retorno curadoria (abr)', 'warn'),
                   _info('Ponto Mais — Ocorrências', '2 ocorrências (mai)', 'warn')],
         'links': [_KRONOS], 'nota_links': _NOTA_KRONOS},
    ],
}
