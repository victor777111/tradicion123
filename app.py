import streamlit as st

st.set_page_config(page_title="Voces del Territorio", page_icon="🌿", layout="wide")

st.markdown("""
<style>
    .stApp {background: linear-gradient(135deg, #f7f4e9 0%, #edf4ec 100%);}
    h1, h2, h3 {color: #214e3d;}
    .hero {padding: 1.4rem; border-radius: 18px; background: #214e3d; color: white;}
    .hero h1 {color: #ffffff;}
    .pill {background:#d9e7d8; padding: .25rem .6rem; border-radius: 20px; color:#214e3d;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🌿 Voces del Territorio</h1>
<p>Comunicación comunitaria · Memoria viva · Turismo responsable</p>
<p>Un prototipo educativo para compartir historias y saberes desde el respeto, la participación y el consentimiento.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
sections = st.tabs(["Inicio", "Territorio", "Saberes vivos", "Noticias", "Participa"])

with sections[0]:
    st.subheader("La comunicación también cuida la memoria")
    st.write("Las tecnologías digitales pueden ayudar a que las comunidades cuenten sus propias historias, fortalezcan su identidad y compartan iniciativas locales.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Enfoque", "Comunitario")
    c2.metric("Herramienta", "Python + IA")
    c3.metric("Principio", "Consentimiento")
    st.info("Pregunta guía: ¿quién cuenta la historia, quién autoriza su publicación y quién se beneficia?")

with sections[1]:
    st.subheader("Turismo comunitario responsable")
    st.write("Ejemplo didáctico: una ruta comunitaria diseñada y gestionada por sus habitantes.")
    st.markdown("- Recorridos guiados por anfitriones locales\n- Gastronomía y emprendimientos comunitarios\n- Caminatas interpretativas con cuidado ambiental\n- Acuerdos claros sobre fotografías, visitas y respeto cultural")
    st.caption("Antes de publicar destinos, precios, rutas o contactos, verificar la información con la comunidad.")

with sections[2]:
    st.subheader("Saberes vivos")
    st.write("Espacio para relatos, técnicas, expresiones artísticas, memoria oral y conocimientos compartidos voluntariamente por sus portadores.")
    st.warning("No todo conocimiento debe hacerse público. Respetar los saberes reservados, la autoría, la lengua y el consentimiento informado.")
    tema = st.selectbox("Explora un ejemplo de contenido", ["Relato oral autorizado", "Técnica artesanal compartida", "Palabras en lengua originaria autorizadas"])
    st.write("Selección:", tema)
    st.write("Ficha sugerida: título, comunidad/autoría autorizada, idioma, fecha, permiso de publicación y contexto.")

with sections[3]:
    st.subheader("Noticias de interés comunitario")
    st.write("Ejemplos de categorías para una futura versión:")
    st.markdown("- Actividades culturales autorizadas\n- Convocatorias y talleres\n- Emprendimientos locales\n- Proyectos de jóvenes y organizaciones")
    st.caption("Cada publicación debe indicar fecha, fuente y contacto responsable cuando corresponda.")

with sections[4]:
    st.subheader("Participa y comparte")
    st.write("Este formulario es una demostración local: no envía ni almacena información.")
    nombre = st.text_input("Nombre o seudónimo (opcional)")
    tipo = st.selectbox("¿Qué te gustaría compartir?", ["Una noticia", "Un relato autorizado", "Una iniciativa comunitaria", "Una corrección"])
    mensaje = st.text_area("Resumen de tu propuesta")
    permiso = st.checkbox("Confirmo que cuento con autorización para compartir este contenido.")
    if st.button("Revisar propuesta"):
        if not mensaje.strip():
            st.error("Escribe un breve resumen para continuar.")
        elif not permiso:
            st.warning("Antes de publicar, se necesita autorización y revisión comunitaria.")
        else:
            st.success("Propuesta preparada para revisión editorial. En esta demo no se envía a ningún servidor.")
            st.write({"nombre": nombre or "Sin nombre", "tipo": tipo, "resumen": mensaje})

st.divider()
st.caption("Prototipo académico · Contenido ilustrativo · No es un portal oficial de la Universidad Amawtay Wasi.")
