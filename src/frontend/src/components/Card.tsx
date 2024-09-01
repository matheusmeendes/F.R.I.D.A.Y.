import React from 'react'

interface CardProps {
  text: string;
}

const Card: React.FC<CardProps> = ({ text }) => {
  return (
    <div className='relative inline-flex justify-start items-end border-2 border-strokeOrange text-strokeOrange py-3 px-[80px] rounded-[14px] h-32 cursor-pointer'>
      {/* Icon at the top left */}
      <div className='absolute inset-0 bg-[#7E7E7E] opacity-0 hover:opacity-30 transition-opacity duration-500 z-0 rounded-[14px]'></div>
      <div className='z-10'>
        <img 
            src="/money.svg" 
            alt="Icon" 
            className="absolute top-[3px] left-[15px] w-3 h-4 mt-4"
        />
        {/* Card text */}
        <span className='absolute left-[15px] bottom-[20px] font-light text-lg text-left'>
          {text.split('\n').map((line, index) => (
            <React.Fragment key={index}>
              {line}
              {index < text.split('\n').length - 1 && <br />}
            </React.Fragment>
          ))}
        </span>
      </div>
    </div>
  )
}

export default Card;
