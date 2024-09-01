import React from 'react'
import Card from './components/Card'

export default function App() {
  return (
    <div 
      className='flex flex-col items-center justify-center min-h-screen bg-cover bg-center' 
      style={{ backgroundImage: "url('/bg.png')" }}
    >
      <img src="/logo.svg" alt="" className='mb-24'/>
      <div className='space-x-8'>
        <Card text={`Tabela de\nTransações`} />
        <Card text={`Tabela de\nTransações`} />
        <Card text={`Tabela de\nTransações`} />
        <Card text={`Tabela de\nTransações`} />
      </div>
    </div>
  )
}
