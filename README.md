Universidad Central del Ecuador
Facultad de Ingeniería y Ciencias Aplicadas
Programación Para Dispositivos Móviles
Nombre: Alexis Mendoza
Curso: SIS10-001
Tema: Evaluación 1

---

# README — Evaluación 1 

Este trabajo consiste en analizar los usuarios que sigue la cuenta de Instagram **@esedgarcia**, utilizando un scraper hecho en Python con Playwright. Después de obtener los datos, se debe analizar qué tipo de contenido consume la cuenta y finalmente explicar cómo esa información podría ayudar a mejorar el UX/UI de una aplicación móvil.  
En mi caso, la app es un sistema para **controlar el subsidio al diésel y registrar las tanqueadas de gasolina de los usuarios**.

Las capturas del programa en ejecución están aquí:  
📎 https://drive.google.com/file/d/1p1klm_FB66IxI4ZNooPqgx3sPXPiDfjd/view?usp=sharing

---

# 1. Proceso realizado

Primero desarrollé un script capaz de iniciar sesión en Instagram usando un archivo `auth.json` y luego abrir la sección de **seguidos (following)** de la cuenta @esedgarcia.  
Al hacer scroll dentro del modal, el programa obtuvo **228 usuarios seguidos**.

Instagram actualmente limita los datos que se pueden extraer, pero sí logré obtener consistentemente:

- username  
- enlace del perfil  

Estos datos son suficientes para hacer un análisis general.

---

# 2. Análisis de los usuarios seguidos

Para este análisis usé el archivo `instagram_following.xlsx`, donde estaban los 228 usernames. Revisando patrones, palabras claves y nombres conocidos, pude clasificar las cuentas en varias categorías.

## 2.1 Categorías predominantes

| Categoría | Cantidad | Porcentaje | Ejemplos |
|----------|----------|------------|----------|
| Personal / Creador | 196 | 86.0% | keevinkn, wendyvane_25 |
| Contenido Local (Ecuador) | 13 | 5.7% | giro.ec, oldbrainecuador |
| Deportes | 7 | 3.1% | lewishamilton, manutd |
| Fitness / Salud | 6 | 2.6% | jeffnippard, maxfitnessquito |
| Fotografía / Video | 4 | 1.8% | ericrubens, camflorys |
| Humor | 1 | 0.4% | kidsgettinghurt |
| Marcas / Ecommerce | 1 | 0.4% | hypewhip |

### ✔ Conclusión  
La gran mayoría de cuentas que sigue son **personas reales o creadores**, no marcas.  
También destaca el contenido **local ecuatoriano**, **deporte**, **fitness** y algo de **fotografía**.

---

# 3. Tipo de contenido que consume @esedgarcia

Basándome en los usuarios seguidos, puedo decir que esta cuenta consume principalmente:

### 🏋️ Contenido de fitness  
Rutinas, motivación, entrenadores, gimnasios.

### ⚽ Contenido deportivo  
Equipos grandes, atletas reconocidos y deportes de combate.

### 📸 Contenido visual / fotografía  
Cuentas de paisajes, viajes y ediciones muy estéticas.

### 🇪🇨 Contenido local  
Emprendimientos ecuatorianos, comida, lugares y eventos.

### 😂 Entretenimiento casual  
Videos de humor o clips cortos.

### ✔ Resumen  
El contenido que le interesa es **motivacional**, **visual**, **deportivo** y **local**.

---

# 4. Influencias, marcas o industrias con mayor presencia

Con los datos obtenidos identifiqué cuatro tipos de influencia más comunes:

1. **Industria deportiva**: cuentas de F1, fútbol y UFC.  
2. **Entrenadores y cultura fitness**.  
3. **Fotografía y contenido estético**.  
4. **Negocios y cultura ecuatoriana**.

Casi no sigue marcas comerciales globales. Esto refuerza la idea de que busca contenido auténtico, visual y cercano.

---

# 5. Patrón de comportamiento o intereses del usuario

Con todo lo anterior, se puede deducir que:

- Le gustan los deportes y el alto rendimiento.  
- Le interesa la salud y mejorar su condición física.  
- Disfruta contenido visualmente atractivo.  
- Tiene identidad local fuerte, consume cosas de Ecuador.  
- Sigue creadores y personas antes que marcas, lo que sugiere que prefiere contenido más humano y real.

### ✔ Comportamiento general deducido  
Es un usuario **activo**, **visual**, **motivacional** y **orientado a su comunidad local**.

---

# 6. ¿Cómo usaría estos datos para el UX/UI de mi APP?

Mi app se enfoca en **registrar las tanqueadas de gasolina y controlar el subsidio al diésel del usuario**. Con base en lo que la cuenta sigue, puedo adaptar la app así:

---

## 6.1 Interfaz muy visual  
Como sigue fotógrafos y contenido estético, usaría:

- tarjetas grandes  
- gráficos simples  
- indicadores visuales del subsidio consumido  

---

## 6.2 Estilo tipo “dashboard” (similar a apps fitness)  
Los usuarios que consumen fitness y deporte suelen preferir ver su progreso.

Aplicaría esto mostrando:

- litros consumidos este mes  
- historial de tanqueadas  
- comparativas entre meses  

---

## 6.3 Información local  
Como consume muchas cuentas de Ecuador, la app puede mostrar:

- estaciones cercanas  
- precios actualizados  
- restricciones por provincia  

---

## 6.4 Lenguaje más humano  
Ya que sigue a muchas personas antes que marcas:

- Notificaciones más amigables  
- Mensajes explicativos claros  
- Feedback motivacional  

---

## 6.5 Navegación sencilla  
Como la mayoría del contenido que consume es simple y directo, el menú recomendado es:

- Registrar tanqueada  
- Historial  
- Estadísticas  
- Perfil  

---

## 6.6 Funciones inspiradas en apps deportivas  
Los usuarios orientados al progreso aprecian visualizar mejoras:

- “Este mes ahorraste X dólares.”  
- “Te falta poco para alcanzar tu meta.”  
- “Reduciste tus tanqueadas en un 15% este mes.”  

---

# 7. Conclusión general

Después del scraping y análisis de los 228 usuarios seguidos:

- Hay un predominio claro de **creadores**, **deporte**, **fitness**, **contenido visual** y **cuentas ecuatorianas**.  
- El usuario consume contenido motivacional y estético, y le interesa su entorno local.  
- Esta información ayuda a diseñar una app más visual, clara, motivadora y enfocada en datos locales.  


