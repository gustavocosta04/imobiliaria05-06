<?php
// Verifica se o email está presente no POST
if (isset($_POST['email'])) {
    // Verifique se o email existe no banco de dados (faça a conexão com o banco de dados aqui)
    // Se o email existir, exclua o cadastro do usuário
    
    // Substitua essa parte pela conexão com o banco de dados e a exclusão do cadastro
    $email = $_POST['email'];
    $deleted = true; // Simulação da exclusão do cadastro

    if ($deleted) {
        echo "Seu cadastro foi excluído. Você pode se cadastrar novamente.";
    } else {
        echo "Erro ao excluir o cadastro. Por favor, tente novamente mais tarde.";
    }
} else {
    echo "Email não fornecido.";
}
?>
