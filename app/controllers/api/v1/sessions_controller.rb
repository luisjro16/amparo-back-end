class Api::V1::SessionsController < ApplicationController
  skip_before_action :authenticate_request, only: [:create]

  def create
      paciente = Paciente.find_by(username: params[:username])
      if paciente&.authenticate(params[:password])
        token = JsonWebToken.encode(paciente_id: paciente.id)
        render json: { token: token }, status: :ok
      else
        render json: { error: 'Credenciais inválidas' }, status: :unauthorized
      end
  end
end
