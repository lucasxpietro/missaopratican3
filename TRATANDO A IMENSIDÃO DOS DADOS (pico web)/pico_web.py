import pandas as pd


def try_convert_date(date_str):
    """
    Tenta converter uma string de data em um objeto datetime usando vários formatos possíveis.
    
    Parâmetros:
    date_str (str): String representando uma data.
    
    Retorna:
    datetime64 ou NaT: Data convertida ou NaT se a conversão falhar.
    """
    if isinstance(date_str, str):
        # Remover aspas simples e espaços extras
        date_str = date_str.replace("'", "").strip()

    # Lista de formatos de data a serem testados
    formats = ['%Y/%m/%d', '%Y-%m-%d', '%d/%m/%Y', '%Y%m%d']
    for fmt in formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except (ValueError, TypeError):
            continue
    return pd.NaT  # Retorna NaT se nenhuma conversão for bem-sucedida

# Ler o arquivo CSV
df = pd.read_csv('dados_pico_web.csv', sep=';', engine='python', encoding='ISO-8859-1')

# Verificar e exibir informações gerais sobre o DataFrame
print("\nInformações Gerais sobre o DataFrame:")
df.info()

# Exibir as primeiras 10 linhas do DataFrame
print("\nPrimeiras 10 Linhas do DataFrame:")
print(df.head(10))

# Exibir as últimas 10 linhas do DataFrame
print("\nÚltimas 10 Linhas do DataFrame:")
print(df.tail(10))

# Criar uma cópia do DataFrame original
df_copia = df.copy()

# Substituir valores nulos na coluna 'Calories' por 0
df_copia['Calories'] = df_copia['Calories'].fillna(0)

# Verificar se a substituição foi bem-sucedida
print("\nDados após substituir valores nulos em 'Calories':")
print(df_copia)

# Substituir valores nulos na coluna 'Date' por '1900/01/01'
df_copia['Date'] = df_copia['Date'].fillna('1900/01/01')

# Verificar se a substituição foi bem-sucedida
print("\nDados após substituir valores nulos em 'Date':")
print(df_copia)

# Aplicar a função personalizada para converter datas
df_copia['Date'] = df_copia['Date'].apply(try_convert_date)

# Substituir a data fictícia '1900/01/01' por NaT
df_copia['Date'] = df_copia['Date'].replace(pd.Timestamp('1900-01-01'), pd.NaT)

# Verificar se a formatação foi corrigida com sucesso
print("\nDados após corrigir formatação de 'Date':")
print(df_copia)

# Remover registros com valores nulos
df_final = df_copia.dropna()

# Verificar se os registros com valores nulos foram removidos
print("\nDados após remover registros com valores nulos:")
print(df_final)

# Salvar o DataFrame final em um novo arquivo CSV
df_final.to_csv('dados_pico_web_limpos.csv', index=False, sep=';', encoding='ISO-8859-1')

print("\nDados limpos salvos em 'dados_pico_web_limpos.csv'")
