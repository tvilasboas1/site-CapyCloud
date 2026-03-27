export default function App() {
  return (
    <div className="min-h-screen bg-slate-900 flex flex-col items-center justify-center p-4">
      <div className="bg-slate-800 p-8 rounded-2xl shadow-2xl border border-slate-700 text-center max-w-md w-full">
        <h1 className="text-4xl font-extrabold text-emerald-400 mb-4 tracking-tight">
          Tailwind ON! 🚀
        </h1>
        
        <p className="text-slate-300 mb-8 text-lg">
          Se você está vendo esta mensagem com um fundo escuro e o título verde, o Tailwind está funcionando perfeitamente.
        </p>

        <button className="bg-emerald-500 hover:bg-emerald-400 text-slate-900 font-bold py-3 px-8 rounded-xl transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-emerald-500/30">
          Pode ir pra casa! 🏠
        </button>
      </div>
    </div>
  )
}