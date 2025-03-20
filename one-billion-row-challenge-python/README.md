# Comparação de Desempenho

Esta tabela compara o desempenho de diferentes ferramentas ao processar **100.000 linhas** e **1.000.000 linhas** de dados com 2 Colunas (station e measure)

<table>
  <thead>
    <tr>
      <th>Biblioteca</th>
      <th>100 mil linhas</th>
      <th>1 milhão linhas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Python_old</td>
      <td>0.13</td>
      <td>1.05</td>
    </tr>
    <tr>
      <td>Python</td>
      <td>0.32</td>
      <td>2.39</td>
    </tr>
    <tr>
      <td>Pandas</td>
      <td>1.50</td>
      <td>1.90</td>
    </tr>
    <tr>
      <td>Dask</td>
      <td>0.42</td>
      <td>0.94</td>
    </tr>
    <tr>
      <td>Duckdb</td>
      <td>0.07</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>Polars</td>
      <td>0.03</td>
      <td>0.12</td>
    </tr>               
  </tbody>
</table>
