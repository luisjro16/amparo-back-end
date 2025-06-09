class RenameSenhaDigestToPasswordDigestOnPacientes < ActiveRecord::Migration[8.0]
  def change
    rename_column :pacientes, :senha_digest, :password_digest
  end
end
