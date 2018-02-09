Sub StockVBAHomework2()


'----------------- For all Worksheets

Dim ws As Worksheet

For Each ws In ThisWorkbook.Sheets

'Set initial variables to hold ticker and volume

Dim ticker_symbol As String
Dim stock_volume As Double
'Set initial volume to 0
stock_volume = 0


'Set initial variable to keep track for each unique ticker symbol in the stock table
 Dim Stock_Table As Integer
  Stock_Table = 2
  

  
'Loop though all stock tickers
    For i = 2 To 797711
 
 'Check if the next ticker matches the previous, set the Ticker Symbol and add to the total stock volume
 
        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
        ticker_symbol = ws.Cells(i, 1).Value
        stock_volume = stock_volume + ws.Cells(i, 7).Value
 
 'Print the ticker symbol in the  table
        ws.Range("I" & Stock_Table).Value = ticker_symbol
 
  'Print the volume in the  table
        ws.Range("J" & Stock_Table).Value = stock_volume
  
  ' Add one to the  table row
       Stock_Table = Stock_Table + 1
    
  'Reset the stock volume
        stock_volume = 0
    
  ' If the cell immediately following a row has the same ticker...
        Else
            stock_volume = stock_volume + ws.Cells(i, 7).Value
    
        End If
    
    Next i

Next ws


End Sub

