# n2_regis_nginx

<h3>"Essa atividade foi top!"<h3/>
  
  Nós quebramos a cabeça mas deu certo! Montamos uma máquina virtual pra rodar o Regis, ai utilizamos o NGINX pra rodar o HTML.
No inicio tentamos utilizar o VSCode, mas nos embananei todo no quesito, fazer o import do Redis.
Então? Resolvemos fazer o básico e trocamos de IDE pro PyCharm e voilà funcionou.
Vídeo em anexo de como funciona.

  <h3>Quais beneficios podem ser obtidos ao utlizar o NGINX:<h3/>
  
  O NGINX é um servidor web poderoso e versátil que traz vários benefícios. Ele é super rápido e escalável, o que significa que pode lidar com muitas solicitações ao mesmo tempo sem ficar lento. Além disso, ele pode distribuir essas solicitações entre diferentes servidores, equilibrando a carga e garantindo que tudo funcione sem problemas. Também tem recursos de cache inteligentes para armazenar conteúdo e acelerar ainda mais o tempo de resposta. Com o NGINX, você pode proteger as comunicações com criptografia SSL e TLS, garantindo que a segurança seja prioridade. Ele é fácil de configurar e tem uma reputação sólida de confiabilidade, então você pode ficar tranquilo sabendo que seu site estará sempre disponível.

<h3>O que acontece se tentar subir dois servidores diferentes na mesma porta da mesma máquina?<h3/>
  
  Pelo que nós entendemos, se você tentar subir dois servidores diferentes na mesma porta da mesma máquina, ocorrerá um conflito de porta, pois cada porta é exclusiva e só pode ser usada por um processo ou aplicativo por vez. Isso resultará em um erro indicando que a porta já está em uso. Para executar vários servidores simultaneamente, é necessário atribuir a cada um deles uma porta exclusiva que não esteja sendo usada por outros aplicativos ou processos no momento. Dessa forma, evita-se o conflito de porta e permite-se a execução simultânea dos servidores na mesma máquina.

<h3>Quando pode ocorrer um erro de Cross-Domain (CORS - Cross-Origin Resource Sharing) e como você pode resolver isso?<h3/>

  Um erro de CORS acontece quando você tenta buscar informações de um lugar na internet, mas é bloqueado pelo navegador por questões de segurança. É como se o navegador dissesse: "Ei, você não pode acessar esse lugar!". Para resolver isso, você pode configurar o servidor para permitir o acesso ou tentar usar alternativas como JSONP, um proxy reverso ou uma API. Essas soluções contornam as restrições de segurança do navegador e permitem que você obtenha as informações que precisa.
