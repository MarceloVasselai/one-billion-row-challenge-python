import polars as pl

# Created by Koen Vossen , 
# Github: https://github.com/koenvo
# Twitter/x Handle: https://twitter.com/mr_le_fox
# https://x.com/mr_le_fox/status/1741893400947839362?s=20

def create_polars_df():
    # Configura o tamanho do chunk para streaming
    pl.Config.set_streaming_chunk_size(100000)
    
    # Lê o arquivo CSV, aplica transformações e coleta os resultados
    return (
        pl.scan_csv(
            "data/measurements.txt",  # Caminho do arquivo
            separator=";",            # Separador de colunas
            has_header=False,         # O arquivo não tem cabeçalho
            new_columns=["station", "measure"],  # Nomes das colunas
            schema={"station": pl.String, "measure": pl.Float64}  # Esquema das colunas
        )
        .group_by(by="station")  # Agrupa por estação
        .agg(
            max=pl.col("measure").max(),  # Calcula o valor máximo
            min=pl.col("measure").min(),  # Calcula o valor mínimo
            mean=pl.col("measure").mean() # Calcula a média
        )
        .sort("station")  # Ordena por estação
        .collect()  # Coleta os resultados (streaming é automático)
    )

if __name__ == "__main__":
    import time

    start_time = time.time()
    df = create_polars_df()
    took = time.time() - start_time
    print(df)
    print(f"Polars Took: {took:.2f} sec")