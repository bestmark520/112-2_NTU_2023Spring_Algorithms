'''
PROCEDURE AnalyzeDynamicTable(expansion_factor, initial_size)
    current_size = initial_size
    table = AllocateTable(current_size)

    WHILE True:
        operation = GetOperation() // 獲得用戶操作：擴展、收縮、退出

        IF operation == "expand":
            new_size = current_size * expansion_factor
            new_table = AllocateTable(new_size)
            CopyElements(table, new_table, current_size)
            DeallocateTable(table)
            table = new_table
            current_size = new_size

        ELSE IF operation == "contract":
            new_size = current_size / expansion_factor
            new_table = AllocateTable(new_size)
            CopyElements(table, new_table, new_size)
            DeallocateTable(table)
            table = new_table
            current_size = new_size

        ELSE IF operation == "exit":
            DeallocateTable(table)
            EXIT

        ELSE:
            PrintError("Invalid operation")

    END WHILE
END PROCEDURE
'''
