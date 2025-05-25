# Sistema de gerenciamento de alunos
class GerenciadorAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, nome, idade, notas):
        aluno = {
            'nome': nome,
            'idade': idade,
            'notas': notas,
            'media': sum(notas) / len(notas)
        }
        self.alunos.append(aluno)

    def buscar_aluno(self, nome):
        for aluno in self.alunos:
            if aluno['nome'] == nome:
                return aluno
        return None

    def alunos_aprovados(self, media_minima=7.0):
        return [aluno for aluno in self.alunos
                if aluno['media'] >= media_minima]

    def estatisticas_turma(self):
        if not self.alunos:
            return None

        medias = [aluno['media'] for aluno in self.alunos]
        return {
            'total_alunos': len(self.alunos),
            'media_geral': sum(medias) / len(medias),
            'maior_media': max(medias),
            'menor_media': min(medias)
        }

# Uso
gerenciador = GerenciadorAlunos()
gerenciador.adicionar_aluno("Ana", 20, [8.5, 9.0, 7.5])
gerenciador.adicionar_aluno("Bruno", 21, [7.0, 6.5, 8.0])
gerenciador.adicionar_aluno("Carlos", 19, [9.5, 9.0, 9.5])

print(gerenciador.estatisticas_turma())
