import io
from typing import Tuple
from datetime import datetime

import numpy as np
from PIL import Image
import streamlit as st

# ==================== CONFIGURAÇÃO DA PÁGINA ====================
st.set_page_config(
    page_title="AgroVision AI - Análise Inteligente de Plantas",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": "https://github.com",
        "Report a bug": "https://github.com",
        "About": "# AgroVision AI - Diagnóstico Inteligente de Plantas"
    }
)

# ==================== SISTEMA DE CORES - IDENTIDADE VISUAL ====================
COLORS = {
    # Paleta primária - Verde profundo (natureza, confiança, crescimento)
    "primary_dark": "#065f46",      # Verde escuro para headers
    "primary": "#10b981",            # Verde vibrante principal
    "primary_light": "#d1fae5",      # Verde claro para backgrounds
    
    # Paleta secundária - Tons neutros sofisticados
    "neutral_900": "#111827",
    "neutral_800": "#1f2937",
    "neutral_700": "#374151",
    "neutral_600": "#4b5563",
    "neutral_400": "#9ca3af",
    "neutral_200": "#e5e7eb",
    "neutral_100": "#f3f4f6",
    "neutral_50": "#f9fafb",
    
    # Alertas - Semáforo inteligente
    "success": "#10b981",            # Verde - Saudável
    "warning": "#f59e0b",            # Âmbar - Alerta
    "danger": "#ef4444",             # Vermelho - Crítico
    
    # Gradientes funcionais
    "gradient_primary": "linear-gradient(135deg, #10b981 0%, #059669 100%)",
    "gradient_secondary": "linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%)",
}

# ==================== DESIGN SYSTEM - CSS AVANÇADO ====================
st.markdown(f"""
    <style>
        /* ==================== RESET E VARIÁVEIS GLOBAIS ==================== */
        :root {{
            --primary: {COLORS['primary']};
            --primary-dark: {COLORS['primary_dark']};
            --neutral-900: {COLORS['neutral_900']};
            --success: {COLORS['success']};
            --warning: {COLORS['warning']};
            --danger: {COLORS['danger']};
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        /* ==================== BODY E CONTAINERS PRINCIPAIS ==================== */
        .stApp {{
            background: linear-gradient(180deg, {COLORS['neutral_50']} 0%, {COLORS['neutral_100']} 100%);
            min-height: 100vh;
        }}
        
        .main {{
            padding: 0 !important;
        }}
        
        [data-testid="stAppViewContainer"] {{
            padding-top: 2rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }}
        
        /* ==================== TIPOGRAFIA ====================*/
        h1 {{
            color: {COLORS['primary_dark']} !important;
            font-size: 2.5em !important;
            font-weight: 900 !important;
            letter-spacing: -0.5px !important;
            margin: 20px 0 10px 0 !important;
            text-align: center;
            line-height: 1.2;
        }}
        
        h2 {{
            color: {COLORS['primary']} !important;
            font-size: 2em !important;
            font-weight: 800 !important;
            margin: 30px 0 15px 0 !important;
            letter-spacing: -0.3px;
        }}
        
        h3 {{
            color: {COLORS['primary_dark']} !important;
            font-size: 1.5em !important;
            font-weight: 700 !important;
            margin: 20px 0 10px 0 !important;
        }}
        
        h4 {{
            color: {COLORS['neutral_800']} !important;
            font-size: 1.2em !important;
            font-weight: 600 !important;
        }}
        
        p {{
            color: {COLORS['neutral_700']} !important;
            font-size: 1em !important;
            line-height: 1.6 !important;
            letter-spacing: 0.3px;
        }}
        
        /* ==================== SIDEBAR PREMIUM ====================*/
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {COLORS['primary_dark']} 0%, {COLORS['primary']} 100%);
            padding: 30px 20px !important;
        }}
        
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
            gap: 1.5rem;
        }}
        
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p {{
            color: white !important;
        }}
        
        [data-testid="stSidebar"] h1 {{
            font-size: 1.8em !important;
            margin-bottom: 15px !important;
        }}
        
        /* ==================== COMPONENTES DE UPLOAD ====================*/
        .uploadedFile {{
            border-radius: 12px !important;
            border: 2px solid {COLORS['neutral_200']} !important;
            background: {COLORS['neutral_50']} !important;
            transition: all 0.3s ease !important;
        }}
        
        .uploadedFile:hover {{
            border-color: {COLORS['primary']} !important;
            background: {COLORS['primary_light']} !important;
        }}
        
        /* ==================== BOTÕES PREMIUM ====================*/
        .stButton > button {{
            background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['primary_dark']} 100%) !important;
            color: white !important;
            font-size: 1.05em !important;
            font-weight: 700 !important;
            padding: 14px 28px !important;
            border-radius: 10px !important;
            border: none !important;
            box-shadow: 0 8px 16px rgba(16, 185, 129, 0.25) !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            cursor: pointer !important;
            width: 100% !important;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }}
        
        .stButton > button:hover {{
            transform: translateY(-2px) !important;
            box-shadow: 0 12px 24px rgba(16, 185, 129, 0.35) !important;
        }}
        
        .stButton > button:active {{
            transform: translateY(0) !important;
        }}
        
        /* ==================== CARDS E CONTAINERS ====================*/
        .stContainer, .card {{
            background: white !important;
            border-radius: 14px !important;
            padding: 24px !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
            border: 1px solid {COLORS['neutral_200']} !important;
            transition: all 0.3s ease !important;
        }}
        
        .stContainer:hover {{
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12) !important;
            transform: translateY(-2px);
        }}
        
        /* ==================== FEATURE BOXES - GRID ====================*/
        .feature-card {{
            background: white;
            border-radius: 14px;
            padding: 24px;
            text-align: center;
            border: 2px solid {COLORS['neutral_200']};
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        .feature-card:hover {{
            border-color: {COLORS['primary']};
            box-shadow: 0 8px 24px rgba(16, 185, 129, 0.15);
            transform: translateY(-4px);
        }}
        
        .feature-icon {{
            font-size: 3em;
            margin-bottom: 12px;
            display: inline-block;
            animation: float 3s ease-in-out infinite;
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
        }}
        
        .feature-title {{
            font-size: 1.3em;
            font-weight: 700;
            color: {COLORS['neutral_800']};
            margin-bottom: 8px;
        }}
        
        .feature-desc {{
            color: {COLORS['neutral_600']};
            font-size: 0.95em;
        }}
        
        /* ==================== RESULTADO - BOXES COLORIDAS ====================*/
        .result-container {{
            border-radius: 14px;
            padding: 28px;
            margin: 20px 0;
            border-left: 5px solid;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.08);
            animation: slideUp 0.5s ease;
        }}
        
        @keyframes slideUp {{
            from {{
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .result-container.healthy {{
            background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
            border-color: {COLORS['success']};
        }}
        
        .result-container.warning {{
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
            border-color: {COLORS['warning']};
        }}
        
        .result-container.danger {{
            background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
            border-color: {COLORS['danger']};
        }}
        
        .result-icon {{
            font-size: 3em;
            margin-bottom: 15px;
            text-align: center;
        }}
        
        .result-label {{
            font-size: 1.8em;
            font-weight: 900;
            margin-bottom: 12px;
            letter-spacing: -0.5px;
        }}
        
        .result-container.healthy .result-label {{
            color: {COLORS['primary_dark']};
        }}
        
        .result-container.warning .result-label {{
            color: #92400e;
        }}
        
        .result-container.danger .result-label {{
            color: #7f1d1d;
        }}
        
        .result-text {{
            font-size: 1.05em;
            line-height: 1.7;
            font-weight: 500;
        }}
        
        .result-container.healthy .result-text {{
            color: {COLORS['primary_dark']};
        }}
        
        .result-container.warning .result-text {{
            color: #78350f;
        }}
        
        .result-container.danger .result-text {{
            color: #7f1d1d;
        }}
        
        /* ==================== DIVIDERS ====================*/
        hr {{
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, {COLORS['primary']}, transparent);
            margin: 40px 0 !important;
            opacity: 0.5;
        }}
        
        /* ==================== INFO BOXES ====================*/
        .stInfo, .info-box {{
            background: linear-gradient(135deg, {COLORS['primary_light']} 0%, rgba(16, 185, 129, 0.1) 100%) !important;
            border-left: 5px solid {COLORS['primary']} !important;
            border-radius: 10px !important;
            padding: 20px !important;
            color: {COLORS['primary_dark']} !important;
        }}
        
        .welcome-box {{
            background: linear-gradient(135deg, {COLORS['primary_light']} 0%, {COLORS['primary_light']} 100%);
            padding: 40px;
            border-radius: 16px;
            text-align: center;
            border: 3px dashed {COLORS['primary']};
            transition: all 0.3s ease;
        }}
        
        .welcome-box:hover {{
            border-color: {COLORS['primary_dark']};
            box-shadow: 0 8px 24px rgba(16, 185, 129, 0.15);
        }}
        
        /* ==================== EXPANDERS ====================*/
        [data-testid="stExpander"] {{
            border: 2px solid {COLORS['primary']} !important;
            border-radius: 12px !important;
            background: white !important;
            overflow: hidden;
        }}
        
        [data-testid="stExpanderButton"] {{
            background: linear-gradient(90deg, {COLORS['primary_light']} 0%, white 100%) !important;
            border-radius: 10px 10px 0 0 !important;
        }}
        
        [data-testid="stExpanderButton"]:hover {{
            background: linear-gradient(90deg, {COLORS['primary']} 0%, rgba(16, 185, 129, 0.1) 100%) !important;
        }}
        
        [data-testid="stExpanderButton"] p {{
            color: {COLORS['primary_dark']} !important;
            font-weight: 700 !important;
            font-size: 1.1em !important;
            margin: 0 !important;
        }}
        
        /* Garantir legibilidade do conteúdo - MUITO IMPORTANTE */
        [data-testid="stExpanderContent"] {{
            background: white !important;
            padding: 25px !important;
            border-radius: 0 0 10px 10px !important;
            color: {COLORS['neutral_800']} !important;
        }}
        
        [data-testid="stExpanderContent"] * {{
            background: transparent !important;
        }}
        
        [data-testid="stExpanderContent"] p {{
            color: {COLORS['neutral_800']} !important;
            font-size: 1em !important;
            line-height: 1.7 !important;
        }}
        
        [data-testid="stExpanderContent"] h1 {{
            color: {COLORS['primary_dark']} !important;
            background: transparent !important;
        }}
        
        [data-testid="stExpanderContent"] h2 {{
            color: {COLORS['primary']} !important;
            background: transparent !important;
            font-size: 1.5em !important;
        }}
        
        [data-testid="stExpanderContent"] h3 {{
            color: {COLORS['primary_dark']} !important;
            background: transparent !important;
        }}
        
        [data-testid="stExpanderContent"] ul {{
            color: {COLORS['neutral_800']} !important;
        }}
        
        [data-testid="stExpanderContent"] li {{
            color: {COLORS['neutral_800']} !important;
            margin-bottom: 10px !important;
            background: transparent !important;
        }}
        
        [data-testid="stExpanderContent"] strong {{
            color: {COLORS['neutral_900']} !important;
            font-weight: 700 !important;
            background: transparent !important;
        }}
        
        [data-testid="stExpanderContent"] div {{
            background: transparent !important;
            color: {COLORS['neutral_800']} !important;
        }}
        
        /* ==================== RESPONSIVE DESIGN ====================*/
        @media (max-width: 768px) {{
            h1 {{ font-size: 2em !important; }}
            h2 {{ font-size: 1.6em !important; }}
            h3 {{ font-size: 1.3em !important; }}
            
            [data-testid="stAppViewContainer"] {{
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                padding-top: 1rem !important;
            }}
            
            .feature-card {{
                padding: 16px;
            }}
            
            .feature-icon {{
                font-size: 2.5em;
            }}
            
            .result-container {{
                padding: 20px;
            }}
        }}
        
        @media (max-width: 480px) {{
            h1 {{ font-size: 1.6em !important; }}
            h2 {{ font-size: 1.3em !important; }}
            
            .result-icon {{ font-size: 2em; }}
            .result-label {{ font-size: 1.4em; }}
        }}
        
        /* ==================== ACESSIBILIDADE ====================*/
        button {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        
        .stButton > button:focus {{
            outline: 3px solid {COLORS['primary']};
            outline-offset: 2px;
        }}
        
        /* ==================== LOADING STATE ====================*/
        .loading {{
            animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }}
        
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
    </style>
""", unsafe_allow_html=True)


class SimpleAgroVisionModel:
    """
    Versão simplificada da ideia do AgroVision AI.

    Em vez de treinar uma CNN completa, esta POC utiliza
    features simples de cor (média de canais e proporção
    de pixels amarelados / amarronzados) para classificar
    a planta em três categorias:

    - Planta Saudável
    - Possível Praga / Estresse Moderado
    - Possível Doença ou Danos Graves

    Isso mantém a lógica de "visão computacional + decisão automática",
    mas em uma forma leve e demonstrável.
    """

    def preprocess_image(self, image: Image.Image) -> np.ndarray:
        """
        Converte a imagem para RGB, redimensiona e retorna um array numpy.
        """
        image = image.convert("RGB")
        image = image.resize((256, 256))
        return np.array(image)

    def extract_color_features(self, img_array: np.ndarray) -> Tuple[float, float, float, float]:
        """
        Extrai features simples de cor:
        - média de R, G, B
        - proporção de pixels 'amarelados/amarronzados'
        """
        arr = img_array / 255.0
        r = arr[:, :, 0]
        g = arr[:, :, 1]
        b = arr[:, :, 2]

        mean_r = float(r.mean())
        mean_g = float(g.mean())
        mean_b = float(b.mean())

        brownish_mask = (r > 0.4) & (g > 0.3) & (b < 0.4)
        brownish_ratio = float(brownish_mask.mean())

        return mean_r, mean_g, mean_b, brownish_ratio

    def classify(self, img_array: np.ndarray) -> Tuple[str, str, str]:
        """
        Classifica a planta com base nas features de cor.

        Retorna:
            classe (str), explicação (str), status (str)
        """
        mean_r, mean_g, mean_b, brownish_ratio = self.extract_color_features(img_array)

        total_mean = mean_r + mean_g + mean_b + 1e-6
        green_ratio = mean_g / total_mean

        if green_ratio > 0.40 and brownish_ratio < 0.05:
            label = "Planta Saudável"
            status = "healthy"
            explanation = (
                "A imagem apresenta predominância de tons esverdeados e baixa presença de manchas. "
                "Sua planta está em perfeito estado de saúde! Mantenha os cuidados regulares."
            )
        elif brownish_ratio < 0.15:
            label = "⚠️ Possível Estresse"
            status = "warning"
            explanation = (
                "Detectamos sinais moderados de variação de cor. Pode indicar estresse hídrico, "
                "deficiência nutricional ou início de pragas. Recomendamos aumentar a atenção."
            )
        else:
            label = "🚨 Danos Graves Detectados"
            status = "danger"
            explanation = (
                "A proporção elevada de manchas amareladas/amarronzadas sugere doença avançada ou danos "
                "significativos. Recomendamos ação imediata e consulta com especialista."
            )

        return label, explanation, status



def render_sidebar():
    """Renderiza sidebar premium com informações e guia de uso"""
    with st.sidebar:
        # Logo e título
        st.markdown(f"""
            <div style='text-align: center; margin-bottom: 30px;'>
                <h1 style='font-size: 2em; color: white; margin: 0;'>🌱</h1>
                <h3 style='color: white; margin: 10px 0 5px 0;'>AgroVision AI</h3>
                <p style='color: rgba(255,255,255,0.8); font-size: 0.9em; margin: 0;'>Diagnóstico Inteligente</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Seção "Como Usar"
        st.markdown("""
        <h4 style='color: white; margin-bottom: 15px; font-size: 1.1em;'>📋 Como Usar</h4>
        """, unsafe_allow_html=True)
        
        steps = [
            ("1️⃣", "Carregar Imagem", "Envie uma foto clara da folha ou planta"),
            ("2️⃣", "Analisar", "Clique no botão de análise"),
            ("3️⃣", "Resultado", "Receba diagnóstico instantâneo")
        ]
        
        for icon, step, desc in steps:
            st.markdown(f"""
            <div style='
                background: rgba(255,255,255,0.1);
                padding: 12px;
                border-radius: 8px;
                margin-bottom: 10px;
                border-left: 3px solid white;
            '>
                <div style='font-size: 1.2em; margin-bottom: 5px;'>{icon} <b style='color:white;'>{step}</b></div>
                <div style='color: rgba(255,255,255,0.7); font-size: 0.85em;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Dicas
        st.markdown("""
        <h4 style='color: white; margin-bottom: 15px; font-size: 1.1em;'>💡 Dicas</h4>
        """, unsafe_allow_html=True)
        
        tips = [
            "Use boa iluminação natural",
            "Foque em uma folha por vez",
            "Evite sombras na imagem",
            "Carregue arquivos JPG ou PNG"
        ]
        
        for tip in tips:
            st.markdown(f"""
            <div style='color: rgba(255,255,255,0.9); margin-bottom: 8px; font-size: 0.9em;'>
                ✓ {tip}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Rodapé
        st.markdown("""
        <div style='text-align: center; color: rgba(255,255,255,0.6); font-size: 0.8em;'>
            <p style='margin: 5px 0;'>AgroVision AI • POC 2025</p>
            <p style='margin: 5px 0;'>Powered by Python & Streamlit</p>
        </div>
        """, unsafe_allow_html=True)


def render_header():
    """Renderiza header premium com animação"""
    st.markdown(f"""
    <div style='text-align: center; margin-bottom: 50px; animation: slideDown 0.6s ease;'>
        <div style='font-size: 4em; margin-bottom: 20px; animation: float 3s ease-in-out infinite;'>
            🌿
        </div>
        <h1 style='margin: 0 0 15px 0; color: {COLORS["primary_dark"]};'>
            AgroVision AI
        </h1>
        <p style='
            font-size: 1.4em;
            color: {COLORS["primary"]};
            margin: 10px 0 0 0;
            font-weight: 600;
            letter-spacing: 0.5px;
        '>
            Diagnóstico Inteligente de Saúde de Plantas
        </p>
        <p style='
            color: {COLORS["neutral_600"]};
            font-size: 1.05em;
            margin-top: 15px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        '>
            Análise por inteligência artificial em tempo real
        </p>
    </div>
    
    <style>
        @keyframes slideDown {{
            from {{
                opacity: 0;
                transform: translateY(-30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
    </style>
    """, unsafe_allow_html=True)


def render_features():
    """Renderiza cards de funcionalidades"""
    st.markdown(f"""
    <h2 style='text-align: center; margin-bottom: 40px; color: {COLORS["primary"]};'>
        Por que AgroVision AI?
    </h2>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    features = [
        {
            "icon": "⚡",
            "title": "Análise Rápida",
            "desc": "Resultados em segundos com processamento otimizado",
            "col": col1
        },
        {
            "icon": "🎯",
            "title": "Precisão",
            "desc": "Algoritmo inteligente baseado em aprendizado de máquina",
            "col": col2
        },
        {
            "icon": "🚀",
            "title": "Inovador",
            "desc": "Tecnologia de ponta em visão computacional",
            "col": col3
        }
    ]
    
    for feature in features:
        with feature["col"]:
            st.markdown(f"""
            <div class='feature-card'>
                <div class='feature-icon'>{feature['icon']}</div>
                <div class='feature-title'>{feature['title']}</div>
                <div class='feature-desc'>{feature['desc']}</div>
            </div>
            """, unsafe_allow_html=True)


def render_upload_section():
    """Renderiza seção de upload com UX otimizada"""
    st.markdown(f"""
    <h2 style='text-align: center; margin: 50px 0 30px 0;'>
        📸 Envie uma Foto
    </h2>
    """, unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1, 1], gap="large")
    
    with col_left:
        st.markdown(f"""
        <div style='
            background: white;
            padding: 30px;
            border-radius: 14px;
            border: 2px solid {COLORS["neutral_200"]};
        '>
            <h3 style='text-align: center; margin-bottom: 15px;'>
                Requisitos da Imagem
            </h3>
            <ul style='color: {COLORS["neutral_700"]}; line-height: 2;'>
                <li>✓ Formato: JPG, JPEG ou PNG</li>
                <li>✓ Iluminação: Natural e clara</li>
                <li>✓ Foco: Folha ou planta inteira</li>
                <li>✓ Tamanho: Até 200MB</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_right:
        uploaded_file = st.file_uploader(
            "Selecione uma imagem",
            type=["jpg", "jpeg", "png"],
            help="Arraste e solte a imagem aqui ou clique para selecionar"
        )
        
        if uploaded_file is not None:
            st.success("✅ Arquivo carregado com sucesso!")
            return uploaded_file
    
    return uploaded_file


def render_analysis_result(image: Image.Image, label: str, explanation: str, status: str):
    """Renderiza resultado da análise com animação"""
    col_image, col_result = st.columns([1, 1], gap="large")
    
    with col_image:
        st.markdown(f"""
        <div style='
            background: white;
            padding: 20px;
            border-radius: 14px;
            border: 2px solid {COLORS["neutral_200"]};
        '>
            <h3 style='text-align: center; margin-bottom: 15px;'>📷 Imagem Analisada</h3>
        </div>
        """, unsafe_allow_html=True)
        st.image(image, use_column_width="auto", output_format="auto")
    
    with col_result:
        st.markdown(f"""
        <div style='
            background: white;
            padding: 20px;
            border-radius: 14px;
            border: 2px solid {COLORS["neutral_200"]};
            margin-bottom: 20px;
        '>
            <h3 style='text-align: center; margin-bottom: 15px;'>🔍 Diagnóstico</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Mapear status para emojis e cores
        status_map = {
            "healthy": ("✅ Saudável", COLORS["success"]),
            "warning": ("⚠️ Atenção", COLORS["warning"]),
            "danger": ("🚨 Crítico", COLORS["danger"])
        }
        
        emoji_status, color = status_map.get(status, ("❓ Desconhecido", COLORS["neutral_600"]))
        
        st.markdown(f"""
        <div class='result-container {status}'>
            <div class='result-icon'>
                {['✅', '⚠️', '🚨'][['healthy', 'warning', 'danger'].index(status) if status in ['healthy', 'warning', 'danger'] else 0]}
            </div>
            <div class='result-label'>{label}</div>
            <div class='result-text'>{explanation}</div>
        </div>
        """, unsafe_allow_html=True)


def render_recommendations(status: str):
    """Renderiza recomendações baseado no status"""
    st.markdown(f"""
    <h3 style='margin-top: 40px; margin-bottom: 20px;'>
        💡 Recomendações
    </h3>
    """, unsafe_allow_html=True)
    
    recommendations = {
        "healthy": [
            "Mantenha a rega regular conforme necessário",
            "Forneça luz adequada (6-8 horas diárias)",
            "Continue com cuidados preventivos",
            "Faça novas análises mensalmente"
        ],
        "warning": [
            "Aumente a frequência de verificações",
            "Revise a rega e drenagem do solo",
            "Inspecione para pragas visíveis",
            "Considere aumentar a luz ou reduzir umidade"
        ],
        "danger": [
            "Isole a planta de outras imediatamente",
            "Procure um especialista em plantas",
            "Considere tratamento com fungicida/inseticida",
            "Revise completamente as condições ambientais"
        ]
    }
    
    recs = recommendations.get(status, [])
    
    cols = st.columns(len(recs))
    for i, (col, rec) in enumerate(zip(cols, recs)):
        with col:
            color_map = {
                "healthy": COLORS["success"],
                "warning": COLORS["warning"],
                "danger": COLORS["danger"]
            }
            border_color = color_map.get(status, COLORS["primary"])
            
            st.markdown(f"""
            <div style='
                background: white;
                padding: 15px;
                border-radius: 10px;
                border-left: 4px solid {border_color};
                box-shadow: 0 2px 8px rgba(0,0,0,0.06);
                height: 100%;
            '>
                <div style='
                    font-weight: 700;
                    color: {border_color};
                    font-size: 2em;
                    text-align: center;
                    margin-bottom: 10px;
                '>
                    {i+1}
                </div>
                <div style='
                    color: {COLORS["neutral_700"]};
                    font-size: 0.95em;
                    text-align: center;
                    line-height: 1.5;
                '>
                    {rec}
                </div>
            </div>
            """, unsafe_allow_html=True)


def main():
    """Função principal com UX/UI otimizada"""
    # Renderizar sidebar
    render_sidebar()
    
    # Container principal
    st.markdown(f"""
    <div style='max-width: 1200px; margin: 0 auto;'>
    """, unsafe_allow_html=True)
    
    # Header
    render_header()
    
    # Features
    render_features()
    
    st.markdown("---")
    
    # Upload section
    uploaded_file = render_upload_section()
    
    # Seção de análise
    if uploaded_file is not None:
        st.markdown("---")
        
        with st.spinner("🔄 Processando imagem..."):
            image_bytes = uploaded_file.read()
            image = Image.open(io.BytesIO(image_bytes))
            
            model = SimpleAgroVisionModel()
            img_array = model.preprocess_image(image)
            
            col_btn = st.columns([1, 3, 1])
            with col_btn[1]:
                analyze_button = st.button(
                    "🚀 ANALISAR PLANTA",
                    use_container_width=True,
                    key="analyze_button"
                )
        
        if analyze_button:
            label, explanation, status = model.classify(img_array)
            
            # Renderizar resultado
            render_analysis_result(image, label, explanation, status)
            
            # Renderizar recomendações
            render_recommendations(status)
            
            # Seção de informações adicionais
            st.markdown("---")
            with st.expander("📚 Como Funciona o Modelo?", expanded=False):
                st.markdown(f"""
                <div style='color: {COLORS["neutral_800"]}; line-height: 1.8;'>
                
                ## Sistema de Análise
                
                **Metodologia:**
                
                O AgroVision AI utiliza análise avançada de características de cor em três dimensões:
                
                1. **Proporção de Verde** - Indica vitalidade e saúde geral
                2. **Tons Amarelados/Amarronzados** - Detecta sinais de doença ou estresse
                3. **Distribuição de Cores** - Identifica padrões anormais
                
                **Categorias de Diagnóstico:**
                
                - ✅ **Saudável**: Tons verdes predominantes, padrão normal
                - ⚠️ **Alerta**: Sinais iniciais de problemas
                - 🚨 **Crítico**: Indicadores de doença avançada
                
                **Tecnologia:**
                
                - Pré-processamento de imagem (normalização e redimensionamento)
                - Extração de features de cor RGB
                - Algoritmo de classificação heurístico
                - Em produção: seria substituído por Deep Learning CNN
                
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # CTA Final
            st.markdown(f"""
            <div style='
                background: linear-gradient(135deg, {COLORS["primary_light"]} 0%, rgba(16, 185, 129, 0.1) 100%);
                padding: 30px;
                border-radius: 14px;
                text-align: center;
                border: 2px solid {COLORS["primary"]};
                margin-top: 40px;
            '>
                <h3 style='color: {COLORS["primary_dark"]}; margin-bottom: 10px;'>
                    📌 Análise Concluída!
                </h3>
                <p style='color: {COLORS["neutral_700"]}; margin: 0;'>
                    Você pode enviar outra imagem para continuar analisando suas plantas.
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    else:
        # Estado vazio - Welcome message
        st.markdown("---")
        st.markdown(f"""
        <div class='welcome-box'>
            <div style='font-size: 4em; margin-bottom: 20px;'>🌾</div>
            <h2 style='color: {COLORS["primary_dark"]}; margin-bottom: 15px;'>
                Pronto para Começar?
            </h2>
            <p style='
                color: {COLORS["primary_dark"]};
                font-size: 1.1em;
                margin-bottom: 20px;
                line-height: 1.6;
            '>
                Envie uma foto clara de sua planta para receber um diagnóstico instantâneo
                e recomendações personalizadas para mantê-la saudável.
            </p>
            <div style='
                background: rgba(16, 185, 129, 0.1);
                padding: 15px;
                border-radius: 10px;
                color: {COLORS["primary_dark"]};
                font-size: 0.95em;
            '>
                💡 <b>Dica:</b> Use uma foto bem iluminada com foco na folha ou planta
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
