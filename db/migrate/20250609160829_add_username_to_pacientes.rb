class AddUsernameToPacientes < ActiveRecord::Migration[8.0]
  def change
    add_column :pacientes, :username, :string
  end
end
