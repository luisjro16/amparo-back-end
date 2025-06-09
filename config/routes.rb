Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      post 'login', to: 'sessions#create'

      get '/health', to: 'health#check'
      resources :medicacoes
      resources :agendamentos
      resources :registro_de_tomadas
      resources :pacientes
    end
  end
end