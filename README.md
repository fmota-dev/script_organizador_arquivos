# Organizador Automático de Arquivos por Tipo

Este script foi criado para **automatizar a organização de arquivos** em pastas específicas com base em suas extensões, sendo útil para manter diretórios organizados, principalmente após processos como digitalizações, downloads ou movimentações de arquivos.

## 🎯 Finalidade

Evitar o acúmulo desordenado de arquivos em uma pasta ao **classificá-los automaticamente por tipo**: Documentos, Imagens, Vídeos, Áudios, Arquivos compactados, Códigos, e Outros.

## 🧠 Como Funciona

- O usuário escolhe uma pasta através de uma interface gráfica.
- O script verifica cada arquivo e identifica sua extensão.
- Os arquivos são movidos para subpastas nomeadas conforme o tipo (por exemplo, `Documentos`, `Imagens`, etc).
- Subpastas são criadas automaticamente caso não existam.

## 📁 Estrutura Criada

Ao rodar o script em uma pasta, ele cria subpastas como:

```
/sua_pasta/
├── Documentos/
├── Imagens/
├── Vídeos/
├── Áudios/
├── Arquivos compactados/
├── Códigos/
└── Outros/
```

## 🖥️ Como Executar

1. Tenha Python instalado no sistema.
2. Execute o script com o comando:

```bash
python main.py
```

3. Escolha a pasta a ser organizada quando a janela aparecer.
4. Os arquivos serão automaticamente realocados para suas respectivas categorias.

## ✅ Tipos de Arquivo Suportados

- **Documentos**: `.pdf`, `.txt`, `.docx`, `.xlsx`, `.xls`, `.pptx`, `.csv`, etc.
- **Imagens**: `.jpg`, `.png`, `.gif`, `.svg`, etc.
- **Vídeos**: `.mp4`, `.mkv`, `.avi`, etc.
- **Áudios**: `.mp3`, `.wav`, `.flac`, etc.
- **Compactados**: `.zip`, `.rar`, `.7z`, `.tar.gz`, etc.
- **Códigos**: `.py`, `.js`, `.html`, `.css`, `.php`, etc.
- **Outros**: arquivos com extensões não mapeadas.

## 💡 Observações

- O script não apaga nenhum arquivo, apenas os move.
- Ideal para pastas de **Downloads**, **Digitalizações**, ou **Backup**.
- Pode ser executado quantas vezes for necessário.

---

🚀 Feito por fmota.dev
