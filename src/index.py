class ActivityDiagram():


dict_activity_diagram = {
  "ActivityDiagramElements": [
    {
        "type": "StartNode",
        "name": "nome do start node"
    },
    {
        "type": "Activity",
        "name": "nome da atividade"
    },
    {
        "type": "DecisionNode",
        "name": "nome do nodo de decisao"
    },
    {
        "type": "MergeNode",
        "name": "nome da atividade"
    },
    {
       "type": "FinalNode",
        "name": "nome do nodo final"
    },
  ],
  "ActivityDiagramTransitions": [
    {
      "name": "transition name",
      "prob": 1,
      "source": "node inicial",
      "target": "node final"
    }
  ]
}

dict_sequence_diagram = {
    "Lifelines": [
        {
            "name": "nome da lifeline"
        },
        {
            "name": "nome da lifeline"
        },
        {
            "name": "nome da lifeline"
        }
    ],
    "Fagments": [
        {
            "type": "Opitional",
            "name": "nome do fragmento",
            "representedBy": "nome do diagrama de sequencia"
        },
        {
            "type": "Opitional",
            "name": "nome do fragmento",
            "representedBy": "nome do diagrama de sequencia"
        },
        {
            "type": "Opitional",
            "name": "nome do fragmento",
            "representedBy": "nome do diagrama de sequencia"
        }
    ],
    "SequenceDiagrams": [
      {
        "name": "nome do diagrama",
        "guard_condition": "condição de guarda",
        "elements": [
            {
                "type": "Message",
                "message_type": "tipo da mensagem",
                "name": "nome da mensagem",
                "prob": "valor da probabilidade",
                "source": "nome da lifeline",
                "target": "nome da lifeline"
            },
            {
                "type": "Message",
                "message_type": "tipo da mensagem",
                "name": "nome da mensagem",
                "prob": "valor da probabilidade",
                "source": "nome da lifeline",
                "target": "nome da lifeline"
            },
            {
                "type": "Fragment",
                "name": " nome do fragmento",
            },
            {
                "type": "Message",
                "message_type": "tipo da mensagem",
                "name": "nome da mensagem",
                "prob": "valor da probabilidade",
                "source": "nome da lifeline",
                "target": "nome da lifeline"
            }
        ],
      },
      {
        "name": "nome do diagrama",
        "guard_condition": "condição de guarda",
        "elements": [
            {
                "type": "Message",
                "message_type": "sync",
                "name": "nome da mensagem",
                "prob": "valor da probabilidade",
                "source": "nome da lifeline",
                "target": "nome da lifeline"
            },
            {
                "type": "Message",
                "message_type": "async",
                "name": "nome da mensagem",
                "prob": "valor da probabilidade",
                "source": "nome da lifeline",
                "target": "nome da lifeline"
            },
            {
                "type": "Fragment",
                "name": " nome do fragmento",
            },
            {
                "type": "Message",
                "message_type": "tipo da mensagem",
                "name": "nome da mensagem",
                "prob": "valor da probabilidade",
                "source": "nome da lifeline",
                "target": "nome da lifeline"
            }
        ],
      },
    ]
}

"""
<ActivityDiagram name=‘‘nome do diagrama’’>
  <ActivityDiagramElements>
    <StartNode name=‘‘nome do nodo inicial’’/>
    <Activity name=‘‘atividade 1’’/>
    <DecisionNode name=‘‘nome do nodo de decisao’’/>
    <Activity name=‘‘atividade 2’’/>
    <MergeNode name=‘‘nome do nodo de fusao’’/>
    <Activity name=‘‘atividade 3’’/>
    <FinalNode name=‘‘nome do nodo final’’/>
  </ActivityDiagramElements> 
  <ActivityDiagramTransitions>
    <Transition source="nome do nodo inicial" target="atividade 1" name=‘‘nome da transicao’’ prob="1" />
    <Transition source="atividade 1" target="atividade 2" name=‘‘nome da transicao’’ prob="1" />
    <Transition source="nome do nodo inicial" target="atividade 1" name=‘‘nome da transicao’’ prob="1" />
    <Transition source="nome do nodo inicial" target="atividade 1" name=‘‘nome da transicao’’ prob="1" />
    <Transition source="nome do nodo inicial" target="atividade 1" name=‘‘nome da transicao’’ prob="1" />
    <Transition source="nome do nodo inicial" target="atividade 1" name=‘‘nome da transicao’’ prob="1" />
    <Transition source="nome do nodo inicial" target="atividade 1" name=‘‘nome da transicao’’ prob="1" />
  </ActivityDiagramTransitions>
</ActivityDiagram>

<SequenceDiagrams>
  <Lifelines>
    <Lifeline name=‘‘nome da lifeline’’ />
    <Lifeline name=‘‘nome da lifeline’’
    <Lifeline name=‘‘nome da lifeline’’ />
  </Lifelines> /> 

  <Fragments>
    <Optional name=‘‘nome do fragmento’’ representedBy=‘‘nome do diagrama de sequencia’’/>
    <Optional name=‘‘nome do fragmento’’ representedBy=‘‘nome do diagrama de sequencia’’/>
    <Optional name=‘‘nome do fragmento’’ representedBy=‘‘nome do diagrama de sequencia’’/>
    ...
  </Fragments>

  <SequenceDiagram name=‘‘atividade 1’’>
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    <Fragment name=‘‘nome do fragmento’’/>
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    ...
  </SequenceDiagram>

  <SequenceDiagram name=‘‘atividade 2’’>
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    <Fragment name=‘‘nome do fragmento’’/>
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    ...
  </SequenceDiagram>

  <SequenceDiagram name=‘‘nome do diagrama’’>
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    <Fragment name=‘‘nome do fragmento’’/>
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    ...
  </SequenceDiagram>
"""

