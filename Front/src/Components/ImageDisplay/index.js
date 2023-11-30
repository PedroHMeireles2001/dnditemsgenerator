import React from 'react'

export default function ImageDisplay({src,alt}) {
  return (
    <img width={"40%"} src={src} alt={alt} />
  )
}
