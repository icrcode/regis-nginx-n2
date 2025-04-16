# n2_regis_nginx
### "Essa atividade foi top!"

Nós quebramos a cabeça, mas deu certo! Montamos uma máquina virtual para rodar o Regis e utilizamos o **NGINX** para servir o HTML. 

No início, tentamos usar o **VSCode**, mas nos embananamos ao tentar importar o Redis. Então, resolvemos simplificar e trocamos para o **PyCharm**, e voilà, funcionou! 

Confira o vídeo em anexo mostrando como tudo funciona.

---

### Quais benefícios podem ser obtidos ao utilizar o NGINX:

O **NGINX** é um servidor web poderoso e versátil que oferece vários benefícios:

- **Alta velocidade e escalabilidade**: Ele pode lidar com muitas solicitações simultaneamente sem perder desempenho.
- **Balanceamento de carga**: Distribui as solicitações entre diferentes servidores, garantindo que tudo funcione de forma eficiente.
- **Recursos de cache inteligentes**: Armazena conteúdos para acelerar ainda mais o tempo de resposta.
- **Segurança**: Oferece suporte a criptografia SSL e TLS, protegendo as comunicações.
- **Confiabilidade**: É reconhecido por sua robustez e facilidade de configuração, garantindo que seu site esteja sempre disponível.

---

### O que acontece se tentar subir dois servidores diferentes na mesma porta da mesma máquina?

Se você tentar rodar dois servidores diferentes na mesma porta da mesma máquina, ocorrerá um **conflito de porta**, já que cada porta é exclusiva e só pode ser usada por um processo ou aplicativo por vez. Isso resultará em um erro informando que a porta já está em uso.

Para evitar esse problema, é necessário atribuir uma **porta exclusiva** a cada servidor. Dessa forma, ambos podem funcionar simultaneamente sem conflitos.

---

### Quando pode ocorrer um erro de Cross-Domain (CORS - Cross-Origin Resource Sharing) e como resolvê-lo?

Um erro de **CORS** acontece quando você tenta acessar recursos de um domínio diferente do que está sendo utilizado, e o navegador bloqueia a solicitação por questões de segurança. É como o navegador dizendo: "Ei, você não pode acessar esse recurso!"

#### Como resolver:
- **Configurar o servidor**: Permitir explicitamente o acesso ao recurso de outro domínio, modificando os cabeçalhos HTTP (como `Access-Control-Allow-Origin`).
- **Usar alternativas**:
  - **JSONP** (em casos específicos, mas menos usado atualmente).
  - **Proxy reverso**: Redireciona as solicitações para o servidor desejado pelo mesmo domínio.
  - **APIs**: Trabalhar com APIs que já suportam CORS.

Essas soluções ajudam a contornar as restrições de segurança do navegador e permitem o acesso aos recursos necessários.
