#!/usr/bin/env node

/**
 * Wrapper para executar o Pacman no CI com tema customizado
 * Este script adapta o index.js original para funcionar no GitHub Actions
 */

const fs = require('fs');
const path = require('path');

// Simula os inputs do GitHub Actions
process.env.INPUT_GITHUB_USER_NAME = process.env.GITHUB_REPOSITORY_OWNER || process.env.INPUT_GITHUB_USER_NAME;
process.env.INPUT_GITHUB_TOKEN = process.env.GITHUB_TOKEN || process.env.INPUT_GITHUB_TOKEN;

console.log('🎮 Iniciando geração do Pacman...');
console.log(`👤 Usuário: ${process.env.INPUT_GITHUB_USER_NAME}`);
console.log(`🔑 Token: ${process.env.INPUT_GITHUB_TOKEN ? '✅ Configurado' : '❌ Não configurado'}`);

// Carrega o tema atual
const themeFile = path.join(__dirname, 'pacman_theme.json');
let currentTheme = 'github-dark';

if (fs.existsSync(themeFile)) {
    try {
        const themeData = JSON.parse(fs.readFileSync(themeFile, 'utf8'));
        currentTheme = themeData.celebration || 'github-dark';
        console.log(`🎨 Tema detectado: ${currentTheme}`);
        console.log(`📝 ${themeData.theme.description}`);
    } catch (error) {
        console.log('⚠️  Erro ao ler tema, usando padrão');
    }
} else {
    console.log('⚠️  Tema não encontrado, usando padrão');
}

// Muda para o diretório da action
const actionDir = path.join(__dirname, '..', 'temp_pacman', 'github-action');
if (fs.existsSync(actionDir)) {
    process.chdir(actionDir);
    console.log(`📂 Diretório: ${actionDir}`);
} else {
    console.log('❌ Diretório da action não encontrado');
    process.exit(1);
}

// Executa a action original
console.log('🚀 Executando geração...\n');

try {
    require('./dist/index.js');
} catch (error) {
    console.error('❌ Erro ao executar action:', error.message);
    process.exit(1);
}

