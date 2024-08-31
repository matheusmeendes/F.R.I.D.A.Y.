# Documentação Pepper

## Grupo - F.R.I.D.A.Y.

## Integrantes:
- <a href="https://www.linkedin.com/in/breno-santana-4a1912228/">Breno Santana</a>
- <a href="https://www.linkedin.com/in/laura-p-bueno/">Laura Bueno</a>
- <a href="https://www.linkedin.com/in/mateus-mar%C3%A7al/">Mateus Marçal</a>
- <a href="https://www.linkedin.com/in/matheusmeendes/">Matheus Mendes</a>
- <a href="https://www.linkedin.com/in/olincosta/">Ólin Medeiros</a>

## Sumário

[1. Introdução](#c1)

[2. Desenvolvimento e Análises de UX e Negócios](#c2)

[3. Análise e exploração dos dados](#c3)

[4. Desenvolvimento da Solução](#c4)

[10. Referências](#c10)

</br>

# <a id="c1"></a>1. Introdução
<p align="justify">
&emsp;&emsp;No cenário atual, onde a agilidade e a eficiência são de grande importância para o sucesso empresarial, a equipe F.R.I.D.A.Y. apresenta Pepper, a assistente virtual financeira projetada para transformar a maneira como as empresas interagem com suas finanças.
</p>

<p align="justify">
&emsp;&emsp;Com o objetivo de capacitar empresas de todos os portes, Pepper oferece acesso instantâneo a informações financeiras personalizadas, análises simplificadas e automação de tarefas, permitindo que os clientes tomem decisões mais estratégicas e otimizem seu tempo.
</p>

<p align="justify">
&emsp;&emsp;Integrando-se ao dashboard do Stark Bank, Pepper proporciona uma experiência intuitiva e acessível, impulsionada por tecnologias de ponta como Processamento de Linguagem Natural (PLN) e Machine Learning. Através da combinação dessas ferramentas e da expertise da equipe F.R.I.D.A.Y., Pepper está pronta para revolucionar a gestão financeira empresarial, tornando-a mais eficiente, personalizada e estratégica.
</p>

<p align="justify">
&emsp;&emsp;Este documento detalhará a jornada de desenvolvimento da Pepper, desde a concepção até a implementação, explorando análises de negócios e UX, a arquitetura da solução, as tecnologias empregadas e os resultados alcançados. Além disso, serão discutidas as lições aprendidas e as perspectivas futuras para o aprimoramento contínuo da assistente virtual, consolidando o compromisso da Stark Bank em oferecer soluções inovadoras e centradas no cliente.
</p>

## 1.1 Objetivos
<p align="justify">
&emsp;&emsp;O projeto Pepper tem como objetivo central capacitar as empresas a gerenciarem suas finanças de forma mais eficiente, estratégica e personalizada, através da implementação de uma assistente virtual financeira inovadora. Para alcançar esse objetivo, Pepper se propõe a fornecer acesso rápido e fácil a informações financeiras, promover a tomada de decisão informada, automatizar tarefas financeiras, personalizar a experiência do usuário, aprimorar a eficiência operacional, dentre outros.
</p>

## 1.2 Proposta da Solução
<p align="justify"> 
&emsp;&emsp;Para concretizar essa visão ambiciosa, Pepper será construída sobre uma arquitetura tecnológica robusta e escalável, utilizando serviços da AWS como base. A solução combinará o poder do Processamento de Linguagem Natural (PLN) para interpretar as solicitações dos usuários com modelos de Machine Learning capazes de aprender e se adaptar continuamente, proporcionando respostas cada vez mais precisas e personalizadas. A integração com a API do Stark Bank garantirá acesso seguro e eficiente aos dados financeiros dos clientes, permitindo que Pepper forneça informações em tempo real e execute tarefas de forma automatizada.
</p>

## 1.3 Justificativa
<p align="justify"> 
&emsp;&emsp;A criação da assistente virtual financeira Pepper se justifica pela crescente necessidade das empresas de otimizar sua gestão financeira, tornando-a mais eficiente, estratégica e personalizada. Em um cenário cada vez mais competitivo e dinâmico, a capacidade de tomar decisões ágeis e embasadas em dados é fundamental para o sucesso empresarial. No entanto, muitas empresas ainda enfrentam desafios como dificuldade em acessar e interpretar informações financeiras, processos manuais e demorados, falta de personalização, custos elevados, dentre outros.
</p>

<p align="justify"> 
&emsp;&emsp;Pepper surge como uma resposta a esses desafios, oferecendo uma solução acessível, eficiente e personalizada para a gestão financeira empresarial. Ao combinar o poder da inteligência artificial com a expertise da equipe Stark Bank, a assistente virtual tem o potencial de democratizar o acesso a informações financeiras, tornando-as mais compreensíveis e acessíveis a todos os usuários, independentemente de seu conhecimento técnico.
</p>

<p align="justify"> 
&emsp;&emsp;Também possui o potencial de automatizar tarefas e otimizar processos, liberando tempo e recursos para que a equipe se concentre em atividades estratégicas e de maior valor agregado. Personalizar a experiência do usuário, oferecendo informações e análises adaptadas às necessidades e ao perfil de cada empresa. Reduzir custos e aumentar a eficiência: Minimizando a necessidade de intervenção humana em tarefas rotineiras e otimizando a gestão financeira. Além de fortalecer o relacionamento com o cliente, oferecendo um serviço inovador e de alto valor agregado, que demonstra o compromisso do Stark Bank em apoiar o sucesso de seus clientes.
</p>

# <a id="c2"></a>2. Desenvolvimento e Análises de UX e Negócios

## 2.1. Domínio de Fundamentos de Negócio

### 2.1.1. Modelo de negócios
<p align="justify"> 
&emsp;&emsp;O modelo de negócios da Pepper, a assistente virtual financeira desenvolvida para o Stark Bank, visa revolucionar a gestão financeira empresarial ao democratizar o acesso à informação e análise de dados. A proposta de valor central da Pepper reside em sua capacidade de fornecer respostas rápidas e personalizadas a perguntas financeiras, gerar insights acionáveis e automatizar tarefas, tudo isso sem a necessidade de conhecimento técnico em SQL ou consulta de dados. A Pepper se integra perfeitamente ao ecossistema Stark Bank, oferecendo suporte personalizado e proativo aos clientes, impulsionando a tomada de decisões estratégicas e a eficiência operacional.
</p>

<p align="center"> 
   Figura 2 - Modelo do Negócio <br> 
   <img src="../assets/modelo_de_negocios.png" style="display: block; margin: auto;" alt="Modelo do Negócio">
   Fonte: Autoria Própria <br>
</p>

<p align="justify"> 
&emsp;&emsp;Em suma, o modelo de negócios da Pepper se destaca por sua proposta de valor centrada no cliente, combinando tecnologia de ponta, dados financeiros e expertise para oferecer uma solução completa e acessível para a gestão financeira empresarial. Ao democratizar o acesso à informação e análise de dados, a Pepper capacita empresas de todos os portes a tomarem decisões mais estratégicas e eficientes, impulsionando seu crescimento e sucesso. A integração com o Stark Bank, o foco em usuários não técnicos e o suporte personalizado garantem uma experiência superior, consolidando a posição da Pepper como uma ferramenta indispensável para a gestão financeira moderna.
</p>

### 2.1.2. Lean Inception
<p align="justify"> 
&emsp;&emsp;A Lean Inception da Pepper, a assistente virtual financeira desenvolvida para o Stark Bank, estabelece uma visão clara do que essa inovadora ferramenta representa e o que ela se propõe a realizar. Pepper é concebida como uma aliada inteligente e personalizada na gestão financeira empresarial, utilizando tecnologias de ponta, como os serviços da Google Cloud para fornecer informações, análises e automação de tarefas, impulsionando a tomada de decisão estratégica. Ao mesmo tempo, a Lean Inception delimita o escopo da Pepper, esclarecendo o que ela não é e o que não faz, garantindo que as expectativas dos usuários estejam alinhadas com suas funcionalidades. Essa definição clara do propósito e dos limites da Pepper é essencial para orientar seu desenvolvimento e garantir que ela atenda às necessidades específicas dos clientes do Stark Bank, impulsionando sua eficiência e sucesso financeiro.
</p>

<p align="center"> 
   Figura 3 - Lean Inception Pepper <br> 
   <img src="../assets/lean_inception.png" style="display: block; margin: auto;" alt="Lean Incepton">
   Fonte: Autoria Própria <br>
</p>

<br>

<p align="justify"> 
&emsp;&emsp;A Lean Inception da Pepper estabeleceu uma base sólida para o desenvolvimento da assistente virtual, definindo claramente seu propósito, funcionalidades e limites. A partir dessa visão, a equipe se dedicou a construir uma solução robusta e escalável, combinando tecnologias de ponta, como Processamento de Linguagem Natural e Machine Learning.
</p>

### 2.1.3. Análise financeira
<p align="justify"> 
&emsp;&emsp;
</p>

## 2.2 Entendimento da Experiência do Usuário

### 2.2.1 Personas
<p align="justify"> 
&emsp;&emsp;
</p>

### 2.2.2 User Stories
<p align="justify"> 
&emsp;&emsp;
</p>

### 2.2.3. Casos de uso
<p align="justify"> 
&emsp;&emsp;
</p>

# <a id="c3"></a>3. Análise e exploração dos dados 

# <a id="c4"></a>4. Desenvolvimento da Solução 

# <a id="c10"></a>10. Referências