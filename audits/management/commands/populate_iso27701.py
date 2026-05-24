from audits.models import Control
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	help = "Popula os controles do ISO 27001"

	def handle(self, *args, **kwargs):
		controls = [
			{
				"code": "A.1.2.2",
				"title": "Identificação e documentação do propósito",
				"description": "A organização deve identificar e documentar os propósitos específicos pelos quais os DP serão tratados. [cite: 1211]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.2.3",
				"title": "Identificação de bases legais",
				"description": "A organização deve determinar, documentar e ser capaz de demonstrar compliance com a base legal pertinente para o tratamento de DP para os propósitos identificados. [cite: 1211]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.2.4",
				"title": "Determinação de quando e como o consentimento deve ser obtido",
				"description": "A organização deve determinar e documentar um processo pelo qual ela pode demonstrar se, quando e como o consentimento para tratamento de DP foi obtido dos titulares de DP. [cite: 1211]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.2.5",
				"title": "Obtenção e registro do consentimento",
				"description": "A organização deve obter e registrar o consentimento dos titulares de DP de acordo com os processos documentados. [cite: 1211]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.2.6",
				"title": "Avaliação de impacto de privacidade",
				"description": "A organização deve avaliar a necessidade de, e implementar onde apropriado, uma avaliação de impacto de privacidade sempre que um novo tratamento de DP ou mudanças no tratamento existente de DP forem planejadas. [cite: 1219]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.2.7",
				"title": "Contratos com operadores de DP",
				"description": "A organização deve ter um contrato escrito com qualquer operador de DP que ela utilize e deve assegurar que seus contratos com operadores de DP contemplem a implementação dos controles apropriados no Anexo A (ver Tabela A.2). [cite: 1219]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.2.8",
				"title": "Controlador conjunto de DP",
				"description": "A organização deve determinar os respectivos papéis e responsabilidades para os operadores de DP (incluindo requisitos de proteção de DP e segurança) com qualquer controlador de conjunto de DP. [cite: 1219]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.2.9",
				"title": "Registros relacionados ao tratamento de DP",
				"description": "A organização deve determinar e manter, de forma segura, os registros necessários ao suporte às suas obrigações para o tratamento de DP. [cite: 1219]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.3.2",
				"title": "Determinação e cumprimento de obrigações com os titulares de DP",
				"description": "A organização deve determinar e documentar suas obrigações legais, regulatórias e de negócios com os titulares de DP, relacionadas ao tratamento de seus DP, e fornecer meios para atender a essas obrigações. [cite: 1219]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.3.3",
				"title": "Determinação das informações para os titulares de DP",
				"description": "A organização deve determinar e documentar a informação a ser fornecida aos titulares de DP relacionadas ao tratamento de seus DP e o momento de tal disponibilização. [cite: 1219]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.3.4",
				"title": "Fornecimento de informações aos titulares de DP",
				"description": "A organização deve fornecer aos titulares de DP, de forma clara e facilmente acessível, informações que identifiquem o controlador de DP e descrevam o tratamento de seus DP. [cite: 1219]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.3.5",
				"title": "Fornecimento de mecanismo para modificar ou retirar o consentimento",
				"description": "A organização deve fornecer um mecanismo para que os titulares de DP modifiquem ou retirem os seus consentimentos. [cite: 1219]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.3.6",
				"title": "Fornecimento de mecanismo para se opor ao tratamento de DP",
				"description": "A organização deve fornecer um mecanismo para os titulares de DP se oporem ao tratamento de seus DP. [cite: 1219]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.3.7",
				"title": "Acesso, correção ou exclusão",
				"description": "A organização deve implementar políticas, procedimentos ou mecanismos para atender às suas obrigações com os titulares de DP para acessarem, corrigirem ou excluírem seus DP. [cite: 1228]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.3.8",
				"title": "Obrigações dos controladores de DP para informar aos terceiros",
				"description": "A organização deve informar aos terceiros com os quais DP tenham sido compartilhados sobre qualquer modificação, retirada ou oposição pertinente aos DP compartilhados, e implementar políticas, procedimentos ou mecanismos apropriados para fazer isso. [cite: 1228]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.3.9",
				"title": "Fornecimento de cópia dos DP tratados",
				"description": "A organização deve ser capaz de fornecer uma cópia dos DP que são tratados, quando requerida pelo titular de DP. [cite: 1228]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.3.10",
				"title": "Tratamento de solicitações",
				"description": "A organização deve definir e documentar políticas e procedimentos para tratamento e resposta a solicitações legítimas dos titulares de DP. [cite: 1228]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.3.11",
				"title": "Tomada de decisão automatizada",
				"description": "A organização deve identify obrigações, incluindo obrigações legais, com os titulares de DP, resultantes de decisões tomadas pela organização, as quais são relativas ao titular de DP, baseadas exclusivamente em tratamento automatizado de DP, e deve be capaz de demonstrar como atende a essas obrigações. [cite: 1228]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.4.2",
				"title": "Limitação da coleta",
				"description": "A organização deve limitar a coleta de DP al mínimo que seja pertinente, proporcional e necessário para os propósitos identificados. [cite: 1228]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.4.3",
				"title": "Limitação do tratamento",
				"description": "A organização deve limitar o tratamento de DP ao que seja adequado, pertinente e necessário para os propósitos identificados. [cite: 1228]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.4.4",
				"title": "Precisão e qualidade",
				"description": "A organização deve assegurar e documentar que os DP sejam precisos, completos e atualizados, quando necessário, para os propósitos para os quais são tratados, ao longo do ciclo de vida dos DP. [cite: 1228]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.4.5",
				"title": "Objetivos de minimização de DP",
				"description": "A organização deve definir e documentar objetivos de minimização de dados e quais mecanismos (como desidentificação) são usados para alcançar aqueles objetivos. [cite: 1228]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.4.6",
				"title": "Desidentificação e exclusão de DP ao final do tratamento",
				"description": "A organização deve excluir os DP ou entregá-los em uma forma que não permita identificação ou reidentificação dos titulares de DP, tão logo os DP originais não sejam mais necessários para o(s) propósito(s) identificado(s). [cite: 1235]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.4.7",
				"title": "Arquivos temporários",
				"description": "A organização deve assegurar que arquivos temporários criados como resultado do tratamento de DP sejam descartados (por exemplo, apagados ou destruídos) seguindo procedimentos documentados dentro de um período de tempo especificado e documentado. [cite: 1235]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.4.8",
				"title": "Retenção",
				"description": "A organização não pode reter DP por período superior ao que seja necessário para os propósitos para os quais os DP sejam tratados. [cite: 1235]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.4.9",
				"title": "Descarte",
				"description": "A organização deve ter políticas, procedimentos ou mecanismos documentados para o descarte de DP. [cite: 1235]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.4.10",
				"title": "Controles de transmissão de DP",
				"description": "A organização deve submeter DP transmitidos (por exemplo, enviados a outra organização) por meio de rede de transmissão de dados aos controles apropriados projetados para assegurar que os dados cheguem ao seu destino pretendido. [cite: 1235]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.5.2",
				"title": "Identificação das bases para transferências de DP entre as jurisdições",
				"description": "A organização deve identificar e documentar as bases pertinentes para transferências de DP entre as jurisdições. [cite: 1235]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.5.3",
				"title": "Países e organizações internacionais para os quais os DP podem ser transferidos",
				"description": "A organização deve especificar e documentar os países e organizações internacionais para os quais os DP podem ser transferidos. [cite: 1235]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.5.4",
				"title": "Registros de transferência de DP",
				"description": "A organização deve registrar transferências de DP para ou de terceiros e assegurar cooperação com aqueles terceiros para apoiar requisições relacionadas com as obrigações com os titulares de DP. [cite: 1235]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.1.5.5",
				"title": "Registros de divulgação de DP a terceiros",
				"description": "A organização deve registrar as divulgações de DP para terceiros, incluindo quais DP foram divulgados, para quem e em que momento. [cite: 1235]",
				"type": "controles para controladores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.2.2",
				"title": "Acordo com o cliente",
				"description": "A organização deve assegurar, onde pertinente, que o contrato para tratar os DP aborde o papel da organização em prestar assistência nas obrigações do cliente (considerando a natureza do tratamento e as informações disponíveis para a organização). [cite: 1243]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.2.3",
				"title": "Propósitos da organização",
				"description": "A organização deve assegurar que os DP tratados em nome de um cliente sejam tratados apenas para os propósitos expressos nas instruções documentadas do cliente. [cite: 1243]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.2.4",
				"title": "Uso para marketing e propaganda",
				"description": "A organização não pode usar os DP tratados sob um contrato para finalidades de marketing e propaganda sem estabelecer que o consentimento prévio foi obtido do respectivo titular de DP. A organização não pode tornar o fornecimento de tal consentimento uma condição para receber o serviço. [cite: 1243]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.2.5",
				"title": "Instruções infratoras",
				"description": "A organização deve informar ao cliente se, em sua opinião, uma instrução de tratamento infringe requisitos legais aplicáveis. [cite: 1243]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.2.6",
				"title": "Obrigações do cliente",
				"description": "A organização deve fornecer ao cliente informações apropriadas para que o cliente possa demonstrar compliance com suas obrigações. [cite: 1243]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.2.7",
				"title": "Registros relativos ao tratamento de DP",
				"description": "A organização deve determinar e manter os registros necessários em apoio à demonstração de compliance com suas obrigações (como especificado no contrato aplicável) para o tratamento de DP conduzido em nome de um cliente. [cite: 1243]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.3.2",
				"title": "Compliance com obrigações para com os titulares de DP",
				"description": "A organização deve fornecer ao cliente os meios para estar em compliance com suas obrigações com os titulares de DP. [cite: 1243]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.4.2",
				"title": "Arquivos temporários",
				"description": "A organização deve assegurar que arquivos temporários criados como resultado do tratamento de DP sejam descartados (por exemplo, apagados ou destruídos) seguindo procedimentos documentados dentro de um período de tempo especificado e documentado. [cite: 1251]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.4.3",
				"title": "Devolução, transferência ou descarte de DP",
				"description": "A organização deve ser capaz de devolver, transferir ou descartar DP de forma segura. Ela deve também tornar sua política disponível para o cliente. [cite: 1251]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.4.4",
				"title": "Controles de transmissão de DP",
				"description": "A organização deve submeter os DP transmitidos por meio de rede de transmissão de dados aos controles apropriados, que sejam projetados para assegurar que os dados cheguem ao seu destino pretendido. [cite: 1251]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.5.2",
				"title": "Fundamentação para a transferência de DP entre as jurisdições",
				"description": "A organização deve informar ao cliente de forma oportuna a fundamentação para as transferências de DP entre as jurisdições e quaisquer alterações pretendidas nesse sentido, para que o cliente possa se opor a tais alterações ou rescindir o contrato. [cite: 1251]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.5.3",
				"title": "Países e organizações internacionais para os quais os DP podem ser transferidos",
				"description": "A organização deve especificar e documentar os países e organizações internacionais para os quais os DP podem ser transferidos. [cite: 1251]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.5.4",
				"title": "Registros de divulgações de DP a terceiros",
				"description": "A organização deve registrar divulgações de DP para terceiros, incluindo quais DP foram divulgados, para quem e em que momento. [cite: 1251]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.5.5",
				"title": "Notificação de solicitações de divulgação de DP",
				"description": "A organização deve notificar o cliente de quaisquer solicitações legalmente obrigatórias de divulgação de DP. [cite: 1251]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.5.6",
				"title": "Divulgações de DP legalmente obrigatórias",
				"description": "A organização deve rejeitar quaisquer solicitações de divulgação de DP que não sejam legalmente obrigatórias, consultar o cliente correspondente antes de realizar any divulgação de DP e aceitar quaisquer solicitações de divulgação de DP acordadas contratualmente e autorizadas pelo cliente correspondente. [cite: 1251]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.5.7",
				"title": "Divulgação de subcontratados utilizados para tratar DP",
				"description": "Antes da utilização, a organização deve informar ao cliente se algum subcontratado é utilizado para tratar DP. [cite: 1259]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.5.8",
				"title": "Envolvimento de subcontratado para tratar os DP",
				"description": "A organização somente deve envolver um subcontratado para tratar os DP conforme previsto no contrato com o cliente. [cite: 1259]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			},
			{
				"code": "A.2.5.9",
				"title": "Troca de subcontratado para tratar os DP",
				"description": "A organização deve, no caso de haver autorização geral por escrito, informar o cliente sobre quaisquer alterações pretendidas relativas à inclusão ou substituição de subcontratados para tratar os DP, dando assim ao cliente a oportunidade de se opor a tais alterações. [cite: 1259]",
				"type": "controles para operadores de DP",
				"iso_type": "ISO 27701"
			}
		]
		Control.objects.bulk_create([Control(**control) for control in controls])