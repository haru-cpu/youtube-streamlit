import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Data Frame')

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
# st.table(df.style.highlight_max(axis=0))

df1 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.60, 139.70],
    columns=['lat', 'lon']
)

st.map(df1)

st.write('display Image')

if st.checkbox('Show Image') :
    img = Image.open('IMG_1943 - コピー.JPG')
    st.image(img, caption='poke', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字は', option, 'です'

st.write('プログレスバーの表示')
'Strart!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

left_colum, right_colum = st.columns(2)
button = left_colum.button('右カラムに文字を表示')
if button:
    right_colum.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせの内容を書く')

option1 = st.text_input('あなたの趣味を教えてください')

condition = st.slider('あなたの今の調子は', 0, 100, 50)

'あなたの趣味:',option1
'コンディション', condition

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""