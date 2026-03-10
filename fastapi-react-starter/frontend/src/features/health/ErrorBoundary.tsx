// import { StatusDot } from '../../components/ui/StatusDot'

// export function ErrorBoundary({ children }) {
//   let error = undefined
//   try {
//     return children
//   } catch (e) {
//     error = e
//   }

//   return (
//     <div className="flex items-center">
//       <StatusDot status="error" />
//       <span className="text-red-600">Error: {error?.message || 'Something went wrong'}</span>
//     </div>
//   )
// }
import { ReactNode, useState } from 'react'

export function ErrorBoundary({ children }: { children: ReactNode }) {
  const [error] = useState<Error | null>(null)

  if (error) {
    return <span className="text-red-600">Error: {error.message || 'Something went wrong'}</span>
  }

  return <>{children}</>
}
