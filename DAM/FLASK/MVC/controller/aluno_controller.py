import model.aluno_model as aluno_model

#listar todos os alunos do database
def listar():
    alunos = aluno_model.getAll()
    if alunos == None:
        return 'Não existem alunos cadastrados. Verifique!'
    return alunos

def localizaPorId(id_consulta):
    aluno = aluno_model.getAlunoId(id_consulta)
    if aluno == None:
        return 'Aluno não encontrado'
    return {'Status': 'Aluno encontrado', "Aluno": aluno}

def localizarPorMaiorMedia():
    alunos = aluno_model.getAlunoMaiorMedia()
    return alunos

def inserirAluno(aluno):
    aluno_model.inserirAluno(aluno)
    return listar()

def excluirPorId(id_deletar):
    aluno = aluno_model.getAlunoId(id_deletar)
    if aluno == None:
        return 'Aluno não encontrado'
    
    aluno_model.excluirAluno(aluno)
    return listar()

def alterarAluno(id_altear, novo_aluno):
    aluno = aluno_model.getAlunoId(id_altear)
    if aluno == None:
        return 'Aluno não econtrado'
    aluno_model.alterarAluno(aluno, novo_aluno)
    return listar()

