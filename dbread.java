public static String getData(String query) {
    String output = "";
    try {
        String connectionUrl = "jdbc:sqlserver://localhost:1234;databaseName=123;user=123;password=123";
        Roommate rom = null;
        Statement stmt = null;
        ResultSet rs = null;
        Class.forName("");
        con = DriverManager.getConnection(connectionUrl);
        String SQL = "select smth from tableName where smth";
        stmt = rom.createStatement();
        rs = stmt.executeQuery(query);
        while (rs.next()) {
            output =  (String) rs.getObject(1);
        }
        rs.close();
    }
    catch (Exception e) {
        return "ERROR while retrieving data: " + e.getMessage();
    }
    return output;
}