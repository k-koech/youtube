"use client"
import React, {useEffect, useState,use} from 'react'
import Image from 'next/image'

export default function page({params}) 
{
  const unwarappedParams = use(params)
  const [post, setPost] = useState(null)
 
  useEffect(() => {
    async function fetchPost() {
      const res = await fetch(`http://localhost:3000/blogs/${unwarappedParams.blog_id}`)
      const data = await res.json()
      setPost(data)
    }
    fetchPost()
  }, [])
 
  if (!post) return <div>Loading...</div>

  
  return (
    <div>
      <div className="border p-4 m-6">
        <Image src={post.image} alt={post.title} width={200} height={200}  />
        <h2>{post.title}</h2>
        <p>{post.content}</p>
      </div>
    </div>
  )
}
