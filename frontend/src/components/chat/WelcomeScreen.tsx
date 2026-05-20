import { cn, hasMessage } from '@/lib/utils';
import { MutableRefObject, useEffect, useMemo, useState } from 'react';

import {
  FileSpec,
  useChatMessages,
  useChatSession,
  useConfig
} from '@chainlit/react-client';

import MessageComposer from './MessageComposer';
import Starters from './Starters';

interface Props {
  fileSpec: FileSpec;
  onFileUpload: (payload: File[]) => void;
  onFileUploadError: (error: string) => void;
  autoScrollRef: MutableRefObject<boolean>;
}

export default function WelcomeScreen(props: Props) {
  const { config } = useConfig();
  const { chatProfile } = useChatSession();
  const { messages } = useChatMessages();
  const [isVisible, setIsVisible] = useState(false);

  const chatProfiles = config?.chatProfiles;

  const allowHtml = config?.features?.unsafe_allow_html;
  const latex = config?.features?.latex;

  useEffect(() => {
    setIsVisible(true);
  }, []);

  // NOTE: Logo display is disabled. To re-enable:
  // 1. If chatProfile has custom icon: return the icon image
  // 2. Otherwise: return <Logo className="w-[200px] mb-2" />
  const logo = useMemo(() => {
    // --- ENABLE LOGO: Uncomment below to show logo ---
    // if (chatProfile && chatProfiles) {
    //   const currentChatProfile = chatProfiles.find(
    //     (cp) => cp.name === chatProfile
    //   );
    //   if (currentChatProfile?.icon) {
    //     return (
    //       <div className="flex flex-col gap-2 mb-2 items-center">
    //         <img
    //           className="h-16 w-16 rounded-full"
    //           src={
    //             currentChatProfile?.icon.startsWith('/public')
    //               ? apiClient.buildEndpoint(currentChatProfile?.icon)
    //               : currentChatProfile?.icon
    //           }
    //         />
    //         {currentChatProfile?.markdown_description ? (
    //           <Markdown
    //             allowHtml={allowHtml}
    //             latex={latex}
    //             renderMarkdown={true}
    //           >
    //             {currentChatProfile.markdown_description}
    //           </Markdown>
    //         ) : null}
    //       </div>
    //     );
    //   }
    // }
    // return <Logo className="w-[200px] mb-2" />;
    // --- END ENABLE LOGO ---
    return null; // Logo disabled - placeholder for future use
  }, [chatProfiles, chatProfile, allowHtml, latex]);

  if (hasMessage(messages)) return null;

  return (
    <div
      id="welcome-screen"
      className={cn(
        'flex flex-col -mt-[60px] gap-4 w-full flex-grow items-center justify-center welcome-screen mx-auto transition-opacity duration-500 opacity-0 delay-100',
        isVisible && 'opacity-100'
      )}
    >
      {logo}
      <MessageComposer {...props} />
      <Starters />
    </div>
  );
}
